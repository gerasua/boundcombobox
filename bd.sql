-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 25, 2020 at 03:48 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `marcas`
--
CREATE DATABASE IF NOT EXISTS `marcas` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `marcas`;

-- --------------------------------------------------------

--
-- Table structure for table `marcas`
--

CREATE TABLE `marcas` (
  `marca` varchar(200) NOT NULL,
  `modelo` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `marcas`
--

INSERT INTO `marcas` (`marca`, `modelo`) VALUES
('Alfa Romeo', 'MiTo'),
('Alfa Romeo', 'Giulietta'),
('Alfa Romeo', '4C'),
('Aston Martin', 'DB9'),
('Aston Martin', 'Rapide'),
('Aston Martin', 'Vanquish'),
('Audi', 'A1'),
('Audi', 'A3'),
('Audi', 'A4');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
