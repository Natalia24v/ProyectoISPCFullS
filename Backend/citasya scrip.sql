SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `citasya` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `citasya` ;

CREATE TABLE IF NOT EXISTS `citasya`.`usuario` (
  `id_usuario` VARCHAR(30) NOT NULL,
  `nombres` VARCHAR(40) NOT NULL,
  `apellido` VARCHAR(30) NOT NULL,
  `edad` INT NOT NULL,
  `genero` CHAR(1) NOT NULL,
  `interes` VARCHAR(100) NOT NULL,
  `bio_personal` VARCHAR(600) NOT NULL,
  `limite_distancia` INT NOT NULL,
  `id_locacion` VARCHAR(64) NOT NULL,
  `rango_edad` INT NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE INDEX `id_usuario` (`id_usuario` ASC) ,
  UNIQUE INDEX `id_locacion` (`id_locacion` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `citasya`.`liked` (
  `like_id` VARCHAR(64) NOT NULL,
  `id_usuario` VARCHAR(30) NOT NULL,
  `lista_likes_dislikes` VARCHAR(100) NOT NULL,
  `id_usuario_likeado` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`like_id`),
  UNIQUE INDEX `like_id` (`like_id` ASC) ,
  UNIQUE INDEX `id_usuario` (`id_usuario` ASC) ,
  UNIQUE INDEX `id_usuario_likeado` (`id_usuario_likeado` ASC) ,
  CONSTRAINT `like_id_usuario_Usuario_id_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `citasya`.`usuario` (`id_usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `citasya`.`locacion` (
  `id_locacion` VARCHAR(64) NOT NULL,
  `nombre_calle` VARCHAR(100) NOT NULL,
  `numero_direccion` INT NOT NULL,
  `barrio` VARCHAR(64) NOT NULL,
  `provincia` VARCHAR(64) NOT NULL,
  `Ciudad` VARCHAR(64) NOT NULL,
  `pais` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id_locacion`),
  UNIQUE INDEX `id_locacion` (`id_locacion` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `citasya`.`superlike` (
  `id_superlike` VARCHAR(64) NOT NULL,
  `id_usuario` VARCHAR(30) NOT NULL,
  `id_usuario_superlikeado` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id_superlike`),
  UNIQUE INDEX `id_superlike` (`id_superlike` ASC) ,
  UNIQUE INDEX `id_usuario` (`id_usuario` ASC) ,
  UNIQUE INDEX `id_usuario_superlikeado` (`id_usuario_superlikeado` ASC) ,
  CONSTRAINT `superlike_id_usuario_Usuario_id_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `citasya`.`usuario` (`id_usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `citasya`.`match1` (
  `id_match` VARCHAR(64) NOT NULL,
  `id_usuario` VARCHAR(30) NOT NULL,
  `id_usuario_likeado` VARCHAR(64) NOT NULL,
  `id_superlike` VARCHAR(64) NOT NULL,
  `bloqueo` VARCHAR(600) NOT NULL,
  PRIMARY KEY (`id_match`),
  UNIQUE INDEX `id_match` (`id_match` ASC) ,
  UNIQUE INDEX `id_usuario` (`id_usuario` ASC) ,
  UNIQUE INDEX `id_usuario_likeado` (`id_usuario_likeado` ASC) ,
  UNIQUE INDEX `id_superlike` (`id_superlike` ASC) ,
  CONSTRAINT `match_id_superlike_superlike_id_superlike`
    FOREIGN KEY (`id_superlike`)
    REFERENCES `citasya`.`superlike` (`id_superlike`),
  CONSTRAINT `match_id_usuario_Usuario_id_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `citasya`.`usuario` (`id_usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `citasya`.`mensajes` (
  `chat_id` VARCHAR(600) NOT NULL,
  `id_match` VARCHAR(64) NOT NULL,
  `receptor` VARCHAR(64) NOT NULL,
  `contenido` VARCHAR(600) NOT NULL,
  `reporte_de_usuario` VARCHAR(600) NOT NULL,
  PRIMARY KEY (`chat_id`),
  UNIQUE INDEX `chat_id` (`chat_id` ASC) ,
  UNIQUE INDEX `id_match` (`id_match` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


CREATE TABLE IF NOT EXISTS `citasya`.`unmatch` (
  `id_usuario` VARCHAR(64) NOT NULL,
  `id_causa` VARCHAR(600) NOT NULL,
  `bloqueado` VARCHAR(600) NOT NULL,
  `reporte_de_usuario` VARCHAR(600) NOT NULL,
  PRIMARY KEY (`id_causa`),
  UNIQUE INDEX `id_usuario` (`id_usuario` ASC) ,
  UNIQUE INDEX `id_causa` (`id_causa` ASC) ,
  CONSTRAINT `unmatch_id_usuario_Usuario_id_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `citasya`.`usuario` (`id_usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `citasya`.`usuariospremiun` (
  `id_usuario_premiun` INT NOT NULL,
  `id_usuariousuario` VARCHAR(30) NOT NULL,
  `plan` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_usuario_premiun`),
  UNIQUE INDEX `id_usuario_UNIQUE` (`id_usuariousuario` ASC) ,
  UNIQUE INDEX `id_usuario_premiun_UNIQUE` (`id_usuario_premiun` ASC) ,
  CONSTRAINT `id_usuario`
    FOREIGN KEY (`id_usuariousuario`)
    REFERENCES `citasya`.`usuario` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
