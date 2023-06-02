use informatica1;

-- Creación de la tabla Responsables
CREATE TABLE Responsables (
  CodigoResponsable INT,
  Nombre VARCHAR(50),
  Apellido VARCHAR(50),
  NumeroDocumento INT,
  Cargo VARCHAR(50),
  PRIMARY KEY (CodigoResponsable)
);

-- Creación de la tabla Ubicaciones
CREATE TABLE Ubicaciones (
  CodigoUbicacion INT,
  NombreUbicacion VARCHAR(100),
  Piso INT,
  PRIMARY KEY (CodigoUbicacion)
);

-- Creación de la tabla Equipos
CREATE TABLE Equipos (
  Serial VARCHAR(50),
  NumeroActivo INT,
  NombreEquipo VARCHAR(100),
  Marca VARCHAR(50),
  CodigoUbicacion INT,
  CodigoResponsable INT,
  PRIMARY KEY (Serial),
  FOREIGN KEY (CodigoUbicacion) REFERENCES Ubicaciones(CodigoUbicacion),
  FOREIGN KEY (CodigoResponsable) REFERENCES Responsables(CodigoResponsable)
);