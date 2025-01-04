
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    balance varchar(20) not null);
CREATE TABLE receive_money (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    money_receive varchar(20) not null,
    day_receive DATE NOT NULL,
    category_of_receive_money VARCHAR(255) NOT NULL,
    note TEXT,
    FOREIGN KEY (username) REFERENCES users(username)
);

CREATE TABLE spend_money (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    money_spend varchar(20) not null,
    day_spend DATE NOT NULL,
    category_of_spend_money VARCHAR(255) NOT NULL,
    note TEXT,
    FOREIGN KEY (username) REFERENCES users(username)
);