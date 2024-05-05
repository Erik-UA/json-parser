import csv

class Action():
    def __init__(self, output_file_path: str) -> None:
        self.csvfile = open(output_file_path, 'w', newline='',
                            encoding='cp1251', errors='replace')
        self.writer = csv.DictWriter(
            self.csvfile, fieldnames=self.write_headers())
        self.writer.writeheader()

    def write_headers(self) -> dict:
        pass

    def parse_action(self, data: dict):
        pass

    def __del__(self):
        self.csvfile.close()
