O programa foi escrito em Python, logo basta fazer py histograma.py para rodar.

Os resultados foram os seguintes utilizando as imagens coloridas:
Com o método Correlation foram 9 acertos (64,28%)
Com o método Chi Square foram 3 acertos (21,42%)
Com o método Intersection foram 12 acertos (85,71%)
Com o método Bhattaryya Distance 13 acertos (92,85&)

Já com as imagens convertidas em tons de cinza os resultados foram:
Com o método Correlation foram 7 acertos (50%)
Com o método Chi Square foram 7 acertos (50%)
Com o método Intersection foram 5 acertos (35,71%)
Com o método Bhattaryya Distance 8 acertos (57,14%)

A taxa de acertos caiu consideravelmente quando as imagens foram convertidas para tons de cinza, exceto quando utilizado o método Chi Square.
Isso se deve ao fato de que muita informação foi perdida na transformação, pois fomos de três canais de cores (rgb) para apenas um.
