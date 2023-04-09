INSERT INTO users(first_name,last_name,gender,login,email,register_date)
VALUES("Sofia","Aleksondrova","girl","Sofiasss333","sofia.gerdeva02@gmail.com",2020-13-12);

INSERT INTO users(first_name,last_name,gender,login,email,register_date)
VALUES("Aleksandr","Kupriyanenko","boy","Aleks547","aleks.kupr@gmail.com",2022-04-10);

INSERT INTO users(first_name,last_name,gender,login,email,register_date)
VALUES("Andry","Ivanov","boy","Andry29","andrysha29@gmail.com",2021-19-11);



INSERT INTO category(category_id,category_title)
VALUES('1','Flower');

INSERT INTO category(category_id,category_title)
VALUES('2','Science');

INSERT INTO category(category_id,category_title)
VALUES('3','Sport');



INSERT INTO posts(title, date_created,content,post_author_id,post_category_id)
VALUES("Как продлить жизнь букету из роз?", 2020-14-12,"Поставьте букет цветов в прохладное место вдали от прямых солнечных лучей, батарей и любых других нагревательных приборов. Не любят розы и сквозняков, от которых их желательно оберегать, чтобы сохранить букет на долгое время. Держите розы отдельно от других цветов, иначе они могут завять гораздо быстрее.", 1, 1);

INSERT INTO posts(title, date_created,content,post_author_id,post_category_id)
VALUES("В чем суть квантовой физики?",2022-07-10,"Квантовая физика — раздел теоретической физики, в котором изучаются квантово-механические и квантово-полевые системы и законы их движения. Основные законы квантовой физики изучаются в рамках квантовой механики и квантовой теории поля, применяются в других разделах физики и других наук.", 2, 2);

INSERT INTO posts(title, date_created,content,post_author_id,post_category_id)
VALUES("В чем смысл занятий спортом?",2021-21-11,"Спорт не только развивает физические качества, но и способствует развитию волевых качеств человека, становлению его как личности. Со временем ребенок привыкает к физическим нагрузкам и спорт становиться образом его жизни.", 3, 3);
