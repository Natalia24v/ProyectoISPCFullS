use citasya;

create TABLE Usuario (
id_usuario VARCHAR(30) PRIMARY KEY NOT NULL UNIQUE,
nombres VARCHAR(40) NOT NULL,
apellido  VARCHAR(30) NOT NULL,
edad INT NOT NULL,
genero CHAR NOT NULL,
interes VARCHAR(100) NOT NULL,
bio_personal VARCHAR(600) NOT NULL,
limite_distancia INT NOT NULL,
id_locacion VARCHAR(64) NOT NULL UNIQUE,
rango_edad INT NOT NULL);

CREATE TABLE locacion (
id_locacion VARCHAR(64) PRIMARY KEY NOT NULL UNIQUE,
nombre_calle VARCHAR(100) NOT NULL,
numero_direccion INT(100) NOT NULL,
barrio VARCHAR(64) NOT NULL,
provincia  VARCHAR(64) NOT NULL,
Ciudad  VARCHAR(64) NOT NULL,
pais VARCHAR(64) NOT NULL);

CREATE TABLE liked (
like_id VARCHAR(64) PRIMARY KEY NOT NULL UNIQUE,
id_usuario VARCHAR(30) NOT NULL UNIQUE,
lista_likes_dislikes VARCHAR(100) NOT NULL,
id_usuario_likeado VARCHAR(64) NOT NULL UNIQUE);

CREATE TABLE superlike (
id_superlike VARCHAR(64) PRIMARY KEY NOT NULL UNIQUE,
id_usuario VARCHAR(30) NOT NULL UNIQUE,
id_usuario_superlikeado VARCHAR(30) NOT NULL UNIQUE);

CREATE TABLE match1 (
id_match VARCHAR(64) PRIMARY KEY NOT NULL UNIQUE,
id_usuario VARCHAR(30) NOT NULL UNIQUE,
id_usuario_likeado VARCHAR(64) NOT NULL UNIQUE,
id_superlike VARCHAR(64) NOT NULL UNIQUE,
bloqueo VARCHAR(600) NOT NULL);

CREATE TABLE mensajes  (
chat_id VARCHAR(600) PRIMARY KEY NOT NULL UNIQUE,
id_match VARCHAR(64) NOT NULL UNIQUE,
receptor VARCHAR(64) NOT NULL,
contenido VARCHAR(600) NOT NULL,
reporte_de_usuario VARCHAR(600) NOT NULL);

CREATE TABLE unmatch (
id_usuario VARCHAR(64) NOT NULL UNIQUE,
id_causa VARCHAR(600) PRIMARY KEY NOT NULL UNIQUE,
bloqueado VARCHAR(600) NOT NULL,
reporte_de_usuario VARCHAR(600) NOT NULL);



ALTER TABLE Usuario ADD CONSTRAINT Usuario_id_locacion_locacion_id_locacion FOREIGN KEY (id_locacion) REFERENCES locacion(id_locacion);
ALTER TABLE liked ADD CONSTRAINT like_id_usuario_Usuario_id_usuario FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario);
ALTER TABLE superlike ADD CONSTRAINT superlike_id_usuario_Usuario_id_usuario FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario);
ALTER TABLE match1 ADD CONSTRAINT match_id_usuario_Usuario_id_usuario FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario);
ALTER TABLE match1 ADD CONSTRAINT match_id_usuario_likeado_like_like_id FOREIGN KEY (id_usuario_likeado) REFERENCES liked(like_id);
ALTER TABLE match1 ADD CONSTRAINT match_id_superlike_superlike_id_superlike FOREIGN KEY (id_superlike) REFERENCES superlike(id_superlike);
ALTER TABLE mensajes  ADD CONSTRAINT mensajes_id_match_match_id_match FOREIGN KEY (id_match) REFERENCES match1(id_match);
ALTER TABLE unmatch ADD CONSTRAINT unmatch_id_usuario_Usuario_id_usuario FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario);
ALTER TABLE unmatch ADD CONSTRAINT unmatch_bloqueado_match_bloqueo FOREIGN KEY (bloqueado) REFERENCES match1(bloqueo);
ALTER TABLE unmatch ADD CONSTRAINT unmatch_reporte_de_usuario_mensajes_reporte_de_usuario FOREIGN KEY (reporte_de_usuario) REFERENCES mensajes (reporte_de_usuario);

select * from mensajessys_configsys_configsys_config