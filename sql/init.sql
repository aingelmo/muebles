CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE dimensions (
    id SERIAL PRIMARY KEY,
    length INT NOT NULL,
    width INT NOT NULL,
    thickness INT NOT NULL,
    price FLOAT NOT NULL,
    article_id INT NOT NULL REFERENCES articles(id)
);

CREATE TABLE materials (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    article_id INT NOT NULL REFERENCES articles(id)
);

CREATE TABLE finishings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    article_id INT NOT NULL REFERENCES articles(id)
);
