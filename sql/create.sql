CREATE TABLE `test_schema`.`natural_disasters` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(256) NOT NULL,
  `created_time` DATETIME NOT NULL,
  `description` MEDIUMTEXT NULL,
  `confidence` DOUBLE NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
COMMENT = 'Table that keeps processed natural disaster records';

CREATE TABLE `test_schema`.`tags` (
  `tag` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`tag`),
  UNIQUE INDEX `tag_UNIQUE` (`tag` ASC))
COMMENT = 'Table that keeps tags to news and disasters';

CREATE TABLE `test_schema`.`natural_disasters_have_tags` (
  `natural_disasters_id` INT UNSIGNED NOT NULL,
  `tag` VARCHAR(32) NOT NULL,
  INDEX `fk_disasters_idx` (`natural_disasters_id` ASC),
  INDEX `fk_tags_idx` (`tag` ASC),
  CONSTRAINT `fk_disasters`
    FOREIGN KEY (`natural_disasters_id`)
    REFERENCES `test_schema`.`natural_disasters` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tags`
    FOREIGN KEY (`tag`)
    REFERENCES `test_schema`.`tags` (`tag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
COMMENT = 'Many-to-many connector for natural_disasters and tags';
