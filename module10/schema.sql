DROP DATABASE IF EXISTS music_app;
CREATE DATABASE IF NOT EXISTS music_app;
USE music_app;

-- Producer entity
CREATE TABLE IF NOT EXISTS artist (
    artist_id INT AUTO_INCREMENT NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    dob DATE NOT NULL,
    PRIMARY KEY (artist_id)
);

-- Consumer entity
CREATE TABLE IF NOT EXISTS consumer (
    consumer_id INT AUTO_INCREMENT NOT NULL,
	email VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (consumer_id)
);

-- Column/field/property entity
CREATE TABLE IF NOT EXISTS genre (
    genre_id INT AUTO_INCREMENT NOT NULL,
	genre_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (genre_id)
);

-- Product/service entity
CREATE TABLE IF NOT EXISTS song (
    song_id INT AUTO_INCREMENT NOT NULL,
    title VARCHAR(255) NOT NULL,
	artist_id INT NULL,
    duration FLOAT NOT NULL,
    is_explicit BOOL NOT NULL,
	song_link VARCHAR(255) NOT NULL,
    PRIMARY KEY (song_id),
	FOREIGN KEY (artist_id) REFERENCES artist(artist_id) ON UPDATE CASCADE ON DELETE SET NULL
);

-- Product/service relationship
CREATE TABLE IF NOT EXISTS song_genres (
    song_id INT NOT NULL,
    genre_id INT NOT NULL,
    PRIMARY KEY (song_id, genre_id),
    FOREIGN KEY (song_id) REFERENCES song(song_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Consumer relationship
CREATE TABLE IF NOT EXISTS consumer_playlist_songs (
    consumer_id INT NOT NULL,
	order_num INT NOT NULL,
    song_id INT NOT NULL,
    PRIMARY KEY (consumer_id, song_id),
    FOREIGN KEY (consumer_id) REFERENCES consumer(consumer_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (song_id) REFERENCES song(song_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Consumer relationship
CREATE TABLE IF NOT EXISTS consumer_favorite_songs (
    consumer_id INT NOT NULL,
    song_id INT NOT NULL,
    PRIMARY KEY (consumer_id, song_id),
    FOREIGN KEY (consumer_id) REFERENCES consumer(consumer_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (song_id) REFERENCES song(song_id) ON UPDATE CASCADE ON DELETE CASCADE
);