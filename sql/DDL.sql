CREATE TABLE public.sales (
	dt date NULL,
	shop_num varchar NULL,
	cash_num varchar NULL,
	doc_id varchar NULL,
	item varchar NULL,
	category varchar NULL,
	amount int4 NULL,
	price int4 NULL,
	discount int4 NULL,
	CONSTRAINT sales_unique UNIQUE (dt, shop_num, cash_num, doc_id, item, category, amount, price, discount)
);