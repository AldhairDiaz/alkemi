SELECT 'CREATE DATABASE alkemi_DB'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'alkemi_DB')\gexec

'\c alkemi_DB'
CREATE TABLE table_all_category (
    cod_localidad integer,
    id_provincia integer,
    id_departamento integer,
    categoria varchar(100),
    provincia varchar(100),
    localidad varchar(100),
    nombre varchar(100),
    domicilio varchar(100),
    codigo_postal varchar(100),
    numero_de_telefono varchar(100),
    mail varchar(100),
    web varchar(100)
);

CREATE TABLE resume_data(
    total_categoria integer,
    total_fuente integer,
    total_provincia_categoria integer

);