CREATE DATABASE IF NOT EXISTS neo4jtest;

USE neo4jtest;

CREATE TABLE IF NOT EXISTS procfact (
  id   bigint    not null,
  pid    int     not null,
  exe    text    not null,
  ppid     int     not null,
  args   text,
  PRIMARY KEY(id));

CREATE TABLE IF NOT EXISTS filefact (
  id   bigint    not null,
  name   text    not null,
  version  text,
  PRIMARY KEY(id));

CREATE TABLE IF NOT EXISTS sockfact (
  id   bigint    not null,
  name   text    not null,
  PRIMARY KEY(id));

CREATE TABLE IF NOT EXISTS nodefact (
  id   bigint    not null,
  type   text,
  PRIMARY KEY(id));

CREATE TABLE IF NOT EXISTS edgefact (
  e_id     bigint    not null,
  n1_hash  bigint    not null,
  n2_hash  bigint    not null,
  relation text     not null,
  sequence bigint    not null,
  session  int     not null,
  timestamp  text,
  primary key(e_id));