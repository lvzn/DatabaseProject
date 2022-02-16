drop table if exists LoginT;

CREATE TABLE LoginT(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login_name VARCHAR(10) NOT NULL,
    login_password VARCHAR(24) NOT NULL
);

drop table if exists User;

CREATE TABLE User(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(20) NOT NULL,
    FOREIGN KEY (id) REFERENCES LoginT (id)
);

drop table if exists Developer;

CREATE TABLE Developer(
    dev_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dev_name VARCHAR(50) NOT NULL
);

drop table if exists Publisher;

CREATE TABLE Publisher(
    pub_id INTEGER PRIMARY KEY AUTOINCREMENT,
    pub_name VARCHAR(50) NOT NULL
);

drop table if exists Composer;

CREATE TABLE Composer(
    comp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    comp_name VARCHAR(50) NOT NULL
);

drop table if exists Game;

CREATE TABLE Game(
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_name VARCHAR(30) NOT NULL,
    game_dev VARCHAR(50) NOT NULL,
    game_pub VARCHAR(50),
    game_comp VARCHAR(50),
    FK_dev_id INT NOT NULL,
    FK_pub_id INT,
    FK_comp_id INT,
    FOREIGN KEY (FK_dev_id) REFERENCES Developer (dev_id),
    FOREIGN KEY (FK_pub_id) REFERENCES Publisher (pub_id),
    FOREIGN KEY (FK_comp_id) REFERENCES Composer (comp_id)
);

drop table if exists User_games;

CREATE TABLE User_games(
    FK_user_id INTEGER PRIMARY KEY,
    FK_game_id INTEGER NOT NULL,    
    purchase_date VARCHAR(20) NOT NULL,
    last_played VARCHAR(20) NOT NULL,
    launched BOOLEAN NOT NULL,
    FOREIGN KEY (FK_user_id) REFERENCES User (id),
    FOREIGN KEY (FK_game_id) REFERENCES Game (game_id)
);

insert into LoginT (login_name, login_password) values 
( "asdfman@gmail.com", "123"),
("qwertygirl@gmail.com", "iloveyou"),
("kebabguy69@hotmail.com", "kebabisbest");

insert into User (username) values 
("ASDFMAN"),
("QWERTYGIRL"),
("K3B4BGUY");

insert into Developer (dev_name) values
("Bethesda Game Studios"),
("ConcernedApe"),
("Valve"),
("Behaviour Interactive Inc."),
("Ubisoft"),
("SEGA"),
("FromSoftware"),
("CD PROJEKT RED");


insert into Publisher (pub_name) values
("Bethesda Softworks"),
("SEGA"),
("Ubisoft"),
("Activision");

insert into Composer (comp_name) values
("Hidenori Shoji"),
("Motoi Sakuraba"),
("Eric Barone"),
("Jeremy Soule"),
("Mike Morasky");

insert into Game (game_name, game_dev, game_pub, game_comp, FK_dev_id, FK_pub_id, FK_comp_id) values
("The Elder Scrolls V: Skyrim", "Bethesda Game Studios", "Bethesda Softworks", "Jeremy Soule", 1, 1, 4),
("Team Fortress 2", "Valve", NULL, "Mike Morasky", 3, NULL, 5),
("Stardew Valley", "ConcernedApe", NULL,  "Eric Barone", 2, NULL, 3),
("Dead by Daylight", "Behaviour Interactive Inc.", NULL, NULL, 4, NULL, NULL),
("Tom Clancy's Rainbow Six Siege", "Ubisoft", NULL, NULL, 5, NULL, NULL),
("Yakuza 0", "SEGA", NULL, "Hidenori Shoji", 6, NULL, 1),
("Sekiro: Shadows Die Twice", "FromSoftware", "Activision", "Motoi Sakuraba", 7, 4, 2),
("Cyberpunk 2077", "CD PROJEKT RED", NULL, NULL, 8, NULL, NULL);



select * from Developer;
