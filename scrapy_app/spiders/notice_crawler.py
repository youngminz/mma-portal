import unicodedata

import scrapy

from notice.models import Notice


class NoticeCrawlerSpider(scrapy.Spider):
    name = 'notice_crawler'
    allowed_domains = ['work.mma.go.kr']

    def scrap_page(self, page):
        url = 'https://work.mma.go.kr/caisBYIS/board/boardList.do'
        params = {
            "gesipan_gbcd": "13",
            "tmpl_id": "1",
            "menu_id": "m_m8_6",
            "pageUnit": "10",
            "pageIndex": str(page),
        }

        return scrapy.FormRequest(method='POST', url=url, formdata=params, callback=self.parse)

    def start_requests(self):
        yield self.scrap_page(1)

    def parse(self, response: scrapy.http.Response):
        # 게시물의 시리얼 넘버 가져오기
        # a 태그의 onclick에 아래처럼 지정되어 있다.
        # javascript:fnBoardView('m_m8_6','13','2000203425','','','1','10');
        # 여기서 2000203425 부분을 가져오면 된다.

        rows = response.xpath('//table[@class="brd_list_n"]/tbody/tr/td/a/@onclick')

        for row in rows:
            serial_number = row.get().split("'")[5]
            url = "https://work.mma.go.kr/caisBYIS/board/boardView.do"
            params = {
                "menu_id": "m_m8_6",
                "gesipan_gbcd": "13",
                "ilryeon_no": serial_number,
                "searchCondition": "",
                "searchKeyword": "",
                "pageIndex": "10",
                "pageUnit": "1",
            }
            yield scrapy.FormRequest(
                method='POST',
                url=url,
                formdata=params,
                callback=self.parse_content,
                meta={'serial_number': serial_number},
            )

        page_info = response.xpath('//div[@class="topics"]').get()

        current_page = int(page_info.split('(')[1].split('/')[0])
        total_page = int(page_info.split('/')[1].split(' ')[0])

        if current_page < total_page:
            yield self.scrap_page(current_page + 1)

    def parse_content(self, response: scrapy.http.Response):
        title, writer, date, _, attachments, content = response.xpath('//form[@id="boardViewform"]//td')

        result = {
            'title': self.normalize_string(title.xpath('text()').get().strip()),
            'writer': self.normalize_string(writer.xpath('text()').get().strip()),
            'date': self.normalize_string(date.xpath('text()').get().strip()),
            'content': self.normalize_string("\n".join(content.xpath('text()').getall())),
            'serial_number': self.normalize_string(response.meta['serial_number']),
        }

        self.save_result(result)

        yield result

    @staticmethod
    def normalize_string(string):
        string = string or ''
        string = unicodedata.normalize('NFKC', string)
        string = string.strip()

        return string

    def save_result(self, params):
        Notice.objects.update_or_create(
            serial_number=params['serial_number'],
            defaults={
                'title': params['title'],
                'writer': params['writer'],
                'date': params['date'],
                'content': params['content'],
            }
        )
