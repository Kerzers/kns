-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: KNS_dev_db
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `name` varchar(60) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES ('C'),('Python'),('SQL');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `teacher_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `text` varchar(1024) NOT NULL,
  `stars` int NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `teacher_id` (`teacher_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`id`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES ('86b4ae9b-3a3a-4226-8a78-cc0c5d5ec850','b073a2d6-2b9a-4e43-bd00-0a63e42581ef','good teacher ',5,'097e0ce6-3f9c-42c2-b9b9-079fbe558eaf','2023-11-25 17:51:16','2023-11-25 17:51:16'),('86b4ae9b-3a3a-4226-8a78-cc0c5d5ec850','b073a2d6-2b9a-4e43-bd00-0a63e42581ef','dsff sdf sdf sdf',5,'20ce9625-9864-44fe-b26a-9ae6f47a6475','2023-11-23 14:27:38','2023-11-23 14:27:38'),('86b4ae9b-3a3a-4226-8a78-cc0c5d5ec850','b073a2d6-2b9a-4e43-bd00-0a63e42581ef','',5,'c27f8510-2f34-436c-89cc-df7d2be6371d','2023-11-25 16:53:37','2023-11-25 16:53:37'),('86b4ae9b-3a3a-4226-8a78-cc0c5d5ec850','b073a2d6-2b9a-4e43-bd00-0a63e42581ef','good teacher',5,'c3f84d68-0953-4af5-a771-d1cc5f080100','2023-11-24 18:01:52','2023-11-24 18:01:52'),('86b4ae9b-3a3a-4226-8a78-cc0c5d5ec850','b073a2d6-2b9a-4e43-bd00-0a63e42581ef','',5,'f94bc3bb-3448-4857-bc45-e07da638729c','2023-11-25 16:53:21','2023-11-25 16:53:21'),('86b4ae9b-3a3a-4226-8a78-cc0c5d5ec850','07924a64-fee0-4a24-90c6-96884e7c00f7','Kerzers is a great teacher ',5,'ff1fa3c9-589f-4801-a7cd-549abbad7361','2023-11-24 16:20:07','2023-11-24 16:20:07');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `user_id` varchar(60) NOT NULL,
  `user_name` varchar(60) DEFAULT NULL,
  `first_name` varchar(60) DEFAULT NULL,
  `last_name` varchar(60) DEFAULT NULL,
  `location` varchar(60) DEFAULT NULL,
  `description` varchar(1024) NOT NULL,
  `course_name` varchar(60) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `course_name` (`course_name`),
  CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `teachers_ibfk_2` FOREIGN KEY (`course_name`) REFERENCES `courses` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES ('b3b00f5d-7f8d-4d88-9190-e4f19841e454','kerzers',NULL,NULL,NULL,'had syda makhdma m3aha ma tal3ba ','C','86b4ae9b-3a3a-4226-8a78-cc0c5d5ec850','2023-11-22 21:00:45','2023-11-22 21:00:45'),('07924a64-fee0-4a24-90c6-96884e7c00f7','Rubis',NULL,NULL,NULL,'I am a good teacher with 5 years experience ','Python','925e2265-4e56-4499-afc2-65fa232978cf','2023-11-24 16:18:51','2023-11-24 16:18:51'),('b3b00f5d-7f8d-4d88-9190-e4f19841e454','kerzers',NULL,NULL,NULL,'kjh kjg jg jhg jkhg ','Python','9f6a4ddd-cea6-4776-b558-d12f849c6201','2023-11-25 22:22:52','2023-11-25 22:22:52'),('b073a2d6-2b9a-4e43-bd00-0a63e42581ef','ryu',NULL,NULL,NULL,'hello im Ryu, In my journey through the realms of computing, I\'ve had the honor of co-creating UNIX and shaping the world with the versatile C programming language, a language that transcends boundaries. Yet, beyond my creations, I\'ve cherished the role of a guide, here to teach and share the wisdom acquired through years of exploration. My approach has always been pragmatic, driven not just by innovation but by the desire to impart knowledge and inspire. Through my work and teachings, I\'ve aimed not only to redefine computing but also to nurture the next wave of tech pioneers, instilling in them the passion that has fueled my own endeavors. and Im hear to teach you C.','C','c3815d39-2e19-4e92-9633-9b5df31c31ae','2023-11-24 18:14:14','2023-11-24 18:14:14'),('b3b00f5d-7f8d-4d88-9190-e4f19841e454','kerzers',NULL,NULL,NULL,'Hey there! I\'m passionate about Python and love sharing its power with eager learners like you.\n\nWith experience in various Python frameworks like Flask and expertise in database management with SQLAlchemy, I\'m here to guide you through your Python journey. Whether you\'re diving into web development, data analysis, or anything in between, I\'ve got your back!\n','Python','eb692c5e-09d6-4cf6-9215-9271d97ee6af','2023-11-25 22:26:09','2023-11-25 22:26:09');
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `email` varchar(60) NOT NULL,
  `password` varchar(128) NOT NULL,
  `user_name` varchar(60) NOT NULL,
  `first_name` varchar(60) DEFAULT NULL,
  `last_name` varchar(60) DEFAULT NULL,
  `location` varchar(60) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('rubis@rubis.com','25d55ad283aa400af464c76d713c07ad','Rubis',NULL,NULL,NULL,'07924a64-fee0-4a24-90c6-96884e7c00f7','2023-11-24 16:18:05','2023-11-24 16:18:05'),('Dinamow@manga.com','0732334c2b190c808eee54f9e8a4d1d1','نيهاهاها',NULL,NULL,NULL,'85d6ad9e-8117-4e0f-b27d-02a0fa0e9df3','2023-11-24 19:40:18','2023-11-24 19:40:18'),('ryu1@ryu.com','25d55ad283aa400af464c76d713c07ad','ryu1',NULL,NULL,NULL,'acada008-b6ca-4dbe-aadc-6ed61ec78b08','2023-11-25 15:56:39','2023-11-25 15:56:39'),('ryu@ryu.com','25d55ad283aa400af464c76d713c07ad','ryu',NULL,NULL,NULL,'b073a2d6-2b9a-4e43-bd00-0a63e42581ef','2023-11-22 20:55:22','2023-11-22 20:55:22'),('kerzers@ryu.com','25d55ad283aa400af464c76d713c07ad','kerzers',NULL,NULL,NULL,'b3b00f5d-7f8d-4d88-9190-e4f19841e454','2023-11-22 20:55:59','2023-11-22 20:55:59');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-26 15:39:40
