import json
import os
from datetime import datetime

DB_FILE = "products.json"

DEFAULT_PRODUCTS = [
    {
        "id": 101,
        "title": "هدفون استودیویی بی‌سیم مدل VX-Pro",
        "price": 8900000,
        "category": "گجت و صدا",
        "badge": "BESTSELLER",
        "desc": "مجهز به درایورهای ۴۵ میلی‌متری نئودیمیوم، حذف نویز فعال (ANC) تطبیقی و ۴۰ ساعت شارژدهی مداوم.",
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=700&q=80"
    },
    {
        "id": 102,
        "title": "کیبورد مکانیکی آلومینیومی 65% کاستوم",
        "price": 6450000,
        "category": "تجهیزات ستاپ",
        "badge": "NEW",
        "desc": "بدنه تمام آلومینیوم CNC شده، سوییچ‌های لاینر روغن‌کاری شده و اتصال سه حالته بی‌سیم.",
        "image": "https://images.unsplash.com/photo-1595225476474-87563907a212?auto=format&fit=crop&w=700&q=80"
    }
]


def load_products():
    if not os.path.exists(DB_FILE):
        save_products(DEFAULT_PRODUCTS)
        return DEFAULT_PRODUCTS
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_products(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[✓] فایل {DB_FILE} با موفقیت بروزرسانی شد ({len(data)} محصول).")


def apply_bulk_price_change(percent):
    products = load_products()
    for p in products:
        new_price = int(p["price"] * (1 + percent / 100))
        # رند کردن به هزار تومان
        p["price"] = round(new_price, -3)
    save_products(products)


if __name__ == "__main__":
    print("=== VORTEX STORE // PYTHON INVENTORY CLI ===")
    print("1. ساخت/بررسی فایل products.json برای گیت‌هاب")
    print("2. اعمال تغییر قیمت درصدی روی کل محصولات (مثلاً 10 یا -15)")
    choice = input("انتخاب کنید (1/2): ").strip()

    if choice == "1":
        items = load_products()
        save_products(items)
    elif choice == "2":
        pct = float(input("درصد تغییر قیمت را وارد کنید (مثلاً -10 برای ۱۰٪ کاهش): "))
        apply_bulk_price_change(pct)