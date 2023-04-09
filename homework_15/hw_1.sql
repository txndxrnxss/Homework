SELECT sum(Bytes) FROM tracks


SELECT SUM (result) FROM (SELECT count(*) as result from employees UNION SELECT count(*) as result from customers)


SELECT Name FROM tracks where AlbumId = (SELECT AlbumId FROM albums where Title = 'A-Sides')


SELECT AlbumId, Title as AlbumName, album_price as AlbumPrice
from albums
INNER JOIN ( 
SELECT AlbumId, SUM(UnitPrice) as album_price
from tracks
GROUP BY AlbumId
)
USING(AlbumId)