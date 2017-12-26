
/* */
select
  product.id,
  product.name,
  price.save / (price.price) as ratio,
  price.price,
  price.save

from product join price
on product.id = price.id
where product.name like "%fish oil%" and date = 1
order by
  ratio desc,
  save desc
limit 100;



select
  product.name,
  date2.price as priceA,
  date2.save as saveA,
  date3.price as priceB,
  date3.price as saveB
from product
join date2
on date2.id = product.id
join date3
on date3.id = product.id