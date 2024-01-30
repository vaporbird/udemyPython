import datetime as dt


class FormatDate():

    @staticmethod
    def input_and_return_formated():
        date = input("input a date you would like your playlist to be created from in {DD-MM-YYYY format}: ").strip()
        while True:
            try:
                split_date = date.split("-")
                if int(split_date[2]) < 1980:
                    raise ValueError("This date is too old")
                if int(split_date[2]) > dt.datetime.now().year + 10:
                    raise ValueError("This date is in the future")
                correct_date = dt.date(
                            year=int(split_date[2]),
                            month=int(split_date[1]),
                            day=int(split_date[0])
                            )

                if dt.datetime.now().date() < correct_date:
                    raise ValueError("This date is in the future")

                pass_date = correct_date.strftime("%Y-%m-%d")
            except (IndexError, ValueError, TypeError) as e:
                if e.__class__ == ValueError:
                    print(str(e))
                date = input("Please enter a valid date{DD-MM-YYYY} ex:05.07.2023: ").strip()
            else:
                return pass_date
