import pandas as pd
from db_to_csv import session
from db_to_csv.models import BookSqlAlchemyItem, Book
from db_to_csv.utils import get_current_date

if __name__ == "__main__":
    all_data = session.query(BookSqlAlchemyItem).all()
    all_data = [book.__dict__ for book in all_data]
    for book in all_data:
        del book["_sa_instance_state"]
        del book["id"]
    books = [Book(**book) for book in all_data]

    df = pd.DataFrame(books)
    df.to_excel(f"books_{get_current_date()}.xlsx")
