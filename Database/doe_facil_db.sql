CREATE DATABASE doefacil_db;

USE doefacil_db;

CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL UNIQUE,
    password VARCHAR(255),
    email VARCHAR(150) NOT NULL UNIQUE,
    active BOOLEAN DEFAULT FALSE,
    name VARCHAR(50),
    phone INT,
    celnumber INT,
    address VARCHAR(150) NOT NULL DEFAULT '',
    document VARCHAR(11) UNIQUE NOT NULL,
    type_document VARCHAR(1) NOT NULL,
    birth_date DATE NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    photo VARCHAR(255)
);


CREATE TABLE Organization (
    id INT AUTO_INCREMENT PRIMARY KEY,
    business_name VARCHAR(255) NOT NULL UNIQUE,
    trading_name VARCHAR(255) NOT NULL UNIQUE,
    document VARCHAR(11) UNIQUE NOT NULL,
    description TEXT,
    incorporation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT FALSE
);

CREATE TABLE Organization_Address (
    id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT,
    street_address VARCHAR(255) NOT NULL,
    address_number VARCHAR(20),
    phone INT,
    city VARCHAR(255) NOT NULL,
    neighborhood VARCHAR(255) NOT NULL,
    state_acronym VARCHAR(2),
    postal_code VARCHAR(15),
    coordinate POINT DEFAULT POINT(0, 0),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (organization_id) REFERENCES Organization(id) ON DELETE CASCADE
);

CREATE TABLE Cause (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL UNIQUE,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT FALSE
);

CREATE TABLE Organization_Causes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT,
    cause_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  	active BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (organization_id) REFERENCES Organization(id) ON DELETE CASCADE,
    FOREIGN KEY (cause_id) REFERENCES Cause(id) ON DELETE CASCADE
);

CREATE TABLE User_Organization_Role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT FALSE
);

CREATE TABLE Users_Organizations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT,
    user_id INT,
    role_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (organization_id) REFERENCES Organization(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES User_Organization_Role(id) ON DELETE CASCADE
);

CREATE TABLE Donation_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255),
    item_quantity INT,
    open_quantity INT
);

CREATE TABLE Donation_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(255)
);

CREATE TABLE Donation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_donation_request INT,
    description TEXT,
    donation_item_id INT,
    donation_user_id_request INT,
    donation_type_id INT,
    FOREIGN KEY (donation_item_id) REFERENCES Donation_item(id) ON DELETE CASCADE,
    FOREIGN KEY (donation_user_id_request) REFERENCES Users_Organizations(id) ON DELETE CASCADE,
    FOREIGN KEY (donation_type_id) REFERENCES Donation_type(id) ON DELETE CASCADE
);
