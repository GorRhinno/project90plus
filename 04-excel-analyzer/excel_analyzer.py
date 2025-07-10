import pandas as pd

def main():
    data_file = pd.read_excel("sales_data.xlsx")

    
    yerevan_data = data_file[data_file["Регион"] == "Yerevan"]
    sell_sum = yerevan_data["Продажи"].sum()
    summary_row = pd.DataFrame([{
        "Дата": "Итого",
        "Регион": None,
        "Продукт": None,
        "Продажи": sell_sum
    }])
    print(yerevan_data)
    print(sell_sum)

    final_data_file = pd.concat([yerevan_data, summary_row,], ignore_index=True)

    final_data_file.to_excel("yerevan_sales.xlsx", index = False)


if __name__ == "__main__":
    main()