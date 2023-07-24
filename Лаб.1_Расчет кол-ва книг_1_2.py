volume_ = 1.44 * 1024 * 1024
quant_page = 100
quant_str = 50
quant_simb = 25
one_symbol = 4
sum_simb = quant_simb * quant_page * quant_str
sum_bite = sum_simb * one_symbol
books_ = volume_ / sum_bite
# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", round(books_))
