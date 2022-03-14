CREATE DATABASE IF NOT EXISTS four_musketeers_trivia_maze
DROP Table if exists questions;
DROP Table if exists games;

CREATE TABLE IF NOT EXISTS questions(ID INTEGER, Category TEXT, Question TEXT, Answer TEXT);

CREATE TABLE IF NOT EXISTS games(ID int AUTO_INCREMENT, name TEXT, game_model TEXT);


