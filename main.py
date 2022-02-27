import vk_api
import sys
from report.parser import parse_arg
from report.vk_api_wrapper import VkApiWrapper
from report.friends_report import FriendsReport
from report.writer.csv_tsv_writer import WriterCsvTsv
from report.writer.json_writer import WriterJson


def main():
    parser = parse_arg(sys.argv[1:])
    token = parser.token
    user_id = parser.user_id
    format_file = parser.format
    catalog = parser.catalog
    session = vk_api.VkApi(token=token)
    vk = session.get_api()
    api = VkApiWrapper(vk)
    report = FriendsReport(api=api)
    data = report.get_data(user_id=user_id)
    data.sort(key=lambda x: x['first_name'])
    try:
        if format_file == 'csv':
            catalog += '/report.csv'
            writer = WriterCsvTsv('\t')
            writer.write(catalog, data)
        elif format_file == 'tsv':
            writer = WriterCsvTsv('\t')
            catalog += '/report.tsv'
            writer.write(catalog, data)
        elif format_file == 'json':
            writer = WriterJson(4)
            catalog += '/report.json'
            writer.write(catalog, data)
        print('Готово')
    except:
        print('Ошибка записи файла')
    return

if __name__ == '__main__':
    main()