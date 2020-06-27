-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 27, 2020 at 02:25 PM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `botto`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
CREATE TABLE IF NOT EXISTS `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pName` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `description` text NOT NULL,
  `available` int(11) NOT NULL,
  `category` varchar(100) NOT NULL,
  `model` varchar(200) NOT NULL,
  `picture` text NOT NULL,
  `picture2` text,
  `picture3` text,
  `mini` int(11) NOT NULL,
  `color` varchar(40) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `keywords` text NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `pName`, `price`, `description`, `available`, `category`, `model`, `picture`, `picture2`, `picture3`, `mini`, `color`, `brand`, `keywords`, `date`) VALUES
(23, 'Combine Harvester Lesney Matchbox 1977 nº 51', 1143, 'Combine Harvester Lesney Matchbox 1977 No. 51 Combine Harvester Measures 7 cm long,\r\n\r\nCategory Farming,\r\n\r\nBase - black\r\n\r\nCasting Year - 1979\r\n\r\nThis model is Made in England', 1, 'farming', 'Combine Harvester No 51e', 'Combine_Harvester1.jpg', 'Combine Harvester2.jpg', 'Combine Harvester3.jpg', 800, 'red', 'Matchbox', 'red farming', '2020-05-03 16:18:26'),
(24, 'Matchbox 1976 \'SUPERFAST\' MB29-C31 Tractor Shovel', 3301, 'Light yellow body, light red shovel, chrome interior & wheel hubs.\r\n\r\nSet from Germany, issued by Lesney in 1977 ,\r\nMade in Germany', 1, 'farming', 'MB29-C31 Tractor Shovel', 'Tractor_Shovel1.jpg', 'Tractor Shovel2.jpg', 'Tractor Shovel3.jpg', 2500, 'yellow', 'Matchbox', 'farming yellow red ', '2020-05-03 16:52:11'),
(25, 'MATCHBOX SERIES, NUMBER 24, ROLLS-ROYCE SILVER SHADOW', 4396, 'ROLLS ROYCE SILVERSHADOW on base. Opening trunk.\r\n\r\nBrand/Number:: Matchbox 24c.\r\n\r\nRolls-Royce Silver Shadow.\r\n\r\nColor/Variation:-Metallic Red.\r\n\r\nDetails- Chrome hubs and black tyres. \r\n\r\nYear 1970,\r\nWeight:- 40g,\r\nLength:- 75 mm\r\n', 1, 'car', 'ROLLS ROYCE', 'ROLLS-ROYCE SILVER SHADOW2.jpg', 'ROLLS-ROYCE_SILVER_SHADOW1.jpg', 'ROLLS-ROYCE SILVER SHADOW3.jpg', 3200, 'pink', 'Matchbox', 'car pink vintage red luxury', '2020-05-03 17:02:08'),
(26, 'Matchbox 23f Atlas Dump Truck', 1947, 'Superfast, orange tipper, grey interior, amber glass. Year: 1982, Weight:\r\n70g', 1, 'truck', 'Atlas Dump Truck', 'Dump_Truck1.jpg', 'Dump Truck2.jpg', 'Dump Truck3.jpg', 1200, 'purple', 'Matchbox', 'purple farming truck', '2020-05-03 18:23:13'),
(27, 'Matchbox 66d Mazda RX500', 500, 'Matchbox Lesney Superfast N°66, Mazda Rx500, 1971, Inglaterr', 1, 'sportscar', 'Mazda RX500', 'Mazda_RX5001.jpg', 'Mazda RX5002.jpg', 'Mazda RX5003.jpg', 300, 'orangle', 'Matchbox', 'orange car sport', '2020-05-03 18:27:15'),
(28, 'Jeep Grand Cherokee', 550, 'Engine: 5.2L V8, \r\nHorsepower: 185 HP', 1, 'jeep', 'Jeep Grand Cherokee', 'Jeep_Grand_Cherokee1.jpg', 'Jeep Grand Cherokee2.jpg', 'Jeep Grand Cherokee3.jpg', 350, 'pink', 'Matchbox', 'pink suv jeep', '2020-05-03 18:49:20'),
(29, 'Porsche VW Brezel Beetle', 2000, 'Description: length: 23 cm, Made in West Germany.\r\nIn good condition', 1, 'bus', 'VW Brezel Beetle', 'Porsche_VW_Brezel_Beetle1.jpg', 'Porsche VW Brezel Beetle2.jpg', 'Porsche VW Brezel Beetle3.jpg', 1500, 'blue', 'DUX', 'blue bus ', '2020-05-07 10:55:55'),
(30, '1950\'S VOLKSWAGEN OVAL WINDOW BEETLE 4 1/2\"', 4587, '1950\'s VW Oval Window Bug by DUX of Germany.  This windup powered German tin toy measures about 4 1/2\" in length.  The windup works well and sends the car running forward.  The front wheels can be turned manually.  The clear plastic windows are all intact.  The plating is all still shiny.  There is some corrosion on the left side of the car which is a bit strange as the rest of the car looks practically new.  Perhaps it sat on its side in a little dampness for years. It is complete, all original and in very good condition.', 1, 'car', 'VOLKSWAGEN OVAL WINDOW BEETLE', 'VOLKSWAGEN_OVAL_WINDOW_BEETLE1.jpg', 'VOLKSWAGEN OVAL WINDOW BEETLE2.jpg', 'VOLKSWAGEN OVAL WINDOW BEETLE3.jpg', 3500, 'Red', 'DUX', 'red car vintage', '2020-05-07 10:58:04'),
(31, 'Nissan GT-R32', 700, 'Popularly known as \"Godzilla\", this was a sports car based on the skyline platform. It soon became the flagship of Nissan performance. Hosting many advance technologies like a four wheel steering and an all wheel drive system.\r\n\r\nEngine: 2.6L inline 6,\r\n\r\nHorsepower: 276 HP.', 1, 'sports car', 'Nissan GT-R', 'Nissan_GT-R1.jpg', 'Nissan GT-R2.jpg', 'Nissan GT-R3.jpg', 420, 'Gray', 'HotWheels', 'gray sport car', '2020-05-07 11:20:52'),
(32, 'Turbo \'95 Mazda RX-7, 43/250 Orange', 700, 'Engine: 1.3L rotary engine\r\n\r\nHorsepower: 101 HP', 1, 'sportscar', '‘95 Mazda RX-7', 'Mazda_RX-71.jpg', 'Mazda RX-72.jpg', 'Mazda RX-73.jpg', 500, 'orange', 'HotWheels', 'orange car sport ', '2020-05-07 11:32:38'),
(33, 'Subaru Impreza 22B STi', 650, 'The 22B STi was the more potent version of the imprezza. Sporting a larger 2.2L engine with better intake and exhaust channels. Capable of producing a whopping 276HP. The blue colour with its golden rims is its iconic look.\r\n\r\nEngine: 2.2L boxer 4\r\n\r\nHorsepower: 276 HP', 1, 'car', 'Subaru Impreza 22B STi', 'Subaru_Impreza_22B_STi1.jpg', 'Subaru Impreza 22B STi2.jpg', 'Subaru Impreza 22B STi3.jpg', 450, 'Dark blue', 'HotWheels', 'blue car', '2020-05-07 11:38:46'),
(34, 'Peterbilt Cabover', 550, 'Engine: 6.7L inline 8\r\n\r\nType: Semi Truck\r\n\r\nHorsepower: 400 HP', 1, 'truck', 'Peterbilt Cabover', 'Peterbilt_Cabover1.jpg', 'Peterbilt Cabover2.jpg', 'Peterbilt Cabover3.jpg', 300, 'Red', 'HotWheels', 'red truck ', '2020-05-07 11:46:10'),
(35, 'The yellow creatures catcher ', 300, 'The Invader made its first run in the 2006 mainline release. It features a plastic rocket that launches from the turret when pressed in the rear. In 2010 the casting lost its missile. And as of 2015 the model lost its double front axles.\r\n', 1, 'war', 'Invader', 'invader1.jpg', 'invader2.jpg', 'invader3.jpg', 150, 'Yellow', 'HotWheels', 'yellow invader war', '2020-05-07 12:01:34'),
(36, 'Chevrolet SSR', 350, 'The SSR is a hardtop convertible pickup truck manufactured by Chevrolet. Produced between 2003 and 2006. Its design was inspired by chevy\'s late 1940\'s pickups and was given a modern retro touch.\r\n', 1, 'car', 'Tarzan the wonder car ', 'Tarzan_the_wonder_car_1.jpg', 'Tarzan the wonder car 2.jpg', 'Tarzan the wonder car 3.jpg', 200, 'Royal Blue', 'HotWheels', 'blue car luxury', '2020-05-07 12:07:37'),
(37, 'Rat Rod Mercedes 280SE', 220, 'A rat rod is a custom car with a worn-down, unfinished appearance. This particular rat rod is based on the Mercedes 280SE.\r\n', 1, 'car', 'Mercedes benz', 'Old_junkyard_mercedes1.jpg', 'Old_junkyard_mercedes1.jpg', 'Old_junkyard_mercedes1.jpg', 150, 'Silver', 'HotWheels', 'gray car luxury', '2020-05-07 12:11:42');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
