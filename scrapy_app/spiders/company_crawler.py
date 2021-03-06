import unicodedata
from urllib.parse import unquote

import scrapy

from company.models import Company, EmploymentHistory


class CompanyCrawlerSpider(scrapy.Spider):
    name = 'company_crawler'
    allowed_domains = ['work.mma.go.kr']

    def scrap_page(self, page):
        url = 'https://work.mma.go.kr/caisBYIS/search/byjjecgeomsaek.do'
        params = {
            "eopjong_gbcd": "1",
            "pageIndex": str(page),
            "pageUnit": "1000",
        }

        return scrapy.FormRequest(method='POST', url=url, formdata=params, callback=self.parse)

    def start_requests(self):
        yield self.scrap_page(1)

    def parse(self, response: scrapy.http.Response):
        rows = response.xpath('//table[@class="brd_list_n"]/tbody/tr')

        for row in rows:
            result = {
                '선정년도': row.xpath('td[1]/text()').get(),
                '지방청': row.xpath('td[2]/text()').get(),
                '채용유무': row.xpath('td[3]/text()').get(),
            }
            link = row.xpath('th/a/@href').get()
            yield response.follow(link, self.parse_content, meta=result)

        page_info = response.xpath('//div[@class="topics"]').get()

        current_page = int(page_info.split('(')[1].split('/')[0])
        total_page = int(page_info.split('/')[1].split(' ')[0])

        if current_page < total_page:
            yield self.scrap_page(current_page + 1)

    def parse_content(self, response: scrapy.http.Response):
        url = response.url
        company_code = unquote(url.split("byjjeopche_cd=")[1].split("&")[0])

        td = response.xpath('//table[1]/tbody/tr/td')

        result = {
            '업체코드': self.normalize_string(company_code),
            '업체명': self.normalize_string(td[0].xpath('text()').get()),
            '주소': self.normalize_string(td[1].xpath('text()').get()),
            '전화번호': self.normalize_phone_number(self.normalize_string(td[2].xpath('text()').get())),
            '팩스번호': self.normalize_phone_number(self.normalize_string(td[3].xpath('text()').get())),
            '업종': self.normalize_string(td[4].xpath('text()').get()),
            '주생산물': self.normalize_string(td[5].xpath('text()').get()),
            '기업규모': self.normalize_string(td[6].xpath('text()').get()),
            '연구분야': self.normalize_string(td[7].xpath('text()').get()),
            '현역배정인원': int(td[8].xpath('text()').get().replace("명", "")),
            '보충역배정인원': int(td[9].xpath('text()').get().replace("명", "")),
            '현역편입인원': int(td[10].xpath('text()').get().replace("명", "")),
            '보충역편입인원': int(td[11].xpath('text()').get().replace("명", "")),
            '현역복무인원': int(td[12].xpath('text()').get().replace("명", "")),
            '보충역복무인원': int(td[13].xpath('text()').get().replace("명", "")),
            '선정년도': self.normalize_string(response.meta['선정년도']),
            '지방청': self.normalize_string(response.meta['지방청']),
            '채용유무': self.normalize_string(response.meta['채용유무']),
        }

        self.save_result(result)

        yield result

    @staticmethod
    def normalize_string(string):
        string = string or ''
        string = unicodedata.normalize('NFKC', string)
        string = string.strip()

        # normalize double space
        string = ' '.join(string.split())

        return string

    @staticmethod
    def normalize_phone_number(string: str):
        # extract number only
        string = ''.join(filter(str.isdecimal, string))

        if string.startswith('02'):
            if len(string) < 3:
                return string
            elif len(string) < 6:
                return string[0:2] + '-' + string[2:]
            elif len(string) < 10:
                return string[0:2] + '-' + string[2:5] + '-' + string[5:]
            else:
                return string[0:2] + '-' + string[2:6] + '-' + string[6:]

        else:
            if len(string) < 4:
                return string
            elif len(string) < 7:
                return string[0:3] + '-' + string[3:]
            elif len(string) < 11:
                return string[0:3] + '-' + string[3:6] + '-' + string[6:]
            else:
                return string[0:3] + '-' + string[3:7] + '-' + string[7:]

    def save_result(self, params):
        company, _ = Company.objects.update_or_create(
            code=params['업체코드'],
            defaults={
                'name': params['업체명'],
                'address': params['주소'],
                'phone_number': params['전화번호'],
                'fax_number': params['팩스번호'],
                'business_type': params['업종'],
                'main_product': params['주생산물'],
                'type': params['기업규모'],
                'research_field': params['연구분야'],
                'department': params['지방청'],
                'selection_year': params['선정년도'],
            }
        )

        EmploymentHistory.objects.create(
            company=company,
            active_duty_assign_count=params['현역배정인원'],
            active_duty_transfer_count=params['현역편입인원'],
            active_duty_in_service_count=params['현역복무인원'],
            supplement_duty_assign_count=params['보충역배정인원'],
            supplement_duty_transfer_count=params['보충역편입인원'],
            supplement_duty_in_service_count=params['보충역복무인원'],
            recruitment_status=params['채용유무'],
        )
