--------------------------------------------------------------------------------
CREATE TABLE `test_schema`.`natural_disasters` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(256) NOT NULL,
  `created_time` DATETIME NOT NULL,
  `description` MEDIUMTEXT NULL,
  `confidence` DOUBLE NULL,
  `reply_count` INT UNSIGNED,
  `favorite_count` INT UNSIGNED,
  `retweet_count` INT UNSIGNED,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
COMMENT = 'Table that keeps processed natural disaster records';

--------------------------------------------------------------------------------
CREATE TABLE `test_schema`.`tags` (
  `tag` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`tag`),
  UNIQUE INDEX `tag_UNIQUE` (`tag` ASC))
COMMENT = 'Table that keeps tags to news and disasters';

--------------------------------------------------------------------------------
CREATE TABLE `test_schema`.`natural_disasters_have_tags` (
  `natural_disasters_id` INT UNSIGNED NOT NULL,
  `tag` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`natural_disasters_id`, `tag`),
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

--------------------------------------------------------------------------------
CREATE TABLE `test_schema`.`news_sources` (
  `name` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
COMMENT = 'List of all news sources that Google News API gives';

--------------------------------------------------------------------------------
CREATE TABLE `test_schema`.`disasters_have_news` (
  `natural_disasters_id` INT UNSIGNED NOT NULL,
  `news_source_name` VARCHAR(64) NOT NULL,
  `count` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`natural_disasters_id`, `news_source_name`),
  INDEX `fk_disasters_idx` (`natural_disasters_id` ASC),
  INDEX `fk_news_sources_idx` (`news_source_name` ASC),
  CONSTRAINT `fk_disasters_to_news`
    FOREIGN KEY (`natural_disasters_id`)
    REFERENCES `test_schema`.`natural_disasters` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_news_sources_to_disasters`
    FOREIGN KEY (`news_source_name`)
    REFERENCES `test_schema`.`news_sources` (`name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
COMMENT = 'Many-to-many link to news sources with amount of how many records were posted on this source about this disaster';
