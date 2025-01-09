-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: facerecognizer
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Dep` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `Semester` varchar(45) DEFAULT NULL,
  `PRN` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Division` varchar(45) DEFAULT NULL,
  `Roll` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `Mobile` varchar(45) DEFAULT NULL,
  `PhotoSample` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`PRN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('Civil','2026','VI','2014110995','Kishan Raj','I','74','Male','7328946325','Yes'),('IT','2024','II','2014111021','Mukesh Kr Mukhiya','III','120','Male','7462955309','Yes'),('ENTC','2024','II','2014111022','Ganesh Kumar','II','121','Male','7322902755','Yes'),('IT','2025','I','2014111028','manish Kumar','II','13','Male','7322902754','Yes'),('IT','2025','I','2014111233','gungun Kumar','II','13','Male','7322902754','Yes'),('IT','2025','I','2014111234','gungun Kumar','II','13','Male','7322902754','Yes'),('IT','2025','I','2014111544','munn Kumar','II','13','Male','7322902754','Yes');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-27 19:14:41
