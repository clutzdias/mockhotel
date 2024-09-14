CREATE DATABASE mockhotel;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

---CRIACAO DAS TABELAS BASE---

CREATE TABLE usuarios (
  usuario uuid NOT NULL DEFAULT uuid_generate_V4(),
  nome character varying(100),
  cpf_cnpj character varying(18),
  telefone character varying(11),
  CONSTRAINT "PK_usuario" PRIMARY KEY (usuario)
);

CREATE TABLE hoteis (
  hotel uuid NOT NULL DEFAULT uuid_generate_V4(),
  cnpj character varying(18),
  nome_fantasia character varying(100),
  razao_social character varying(100),
  classificacao character varying(50),
  CONSTRAINT "PK_hotel" PRIMARY KEY (hotel)    
);

CREATE TABLE quartos (
  quarto uuid NOT NULL DEFAULT uuid_generate_V4(),
  hotel uuid NOT NULL,
  quantidade_acomodacoes smallint,
  tipo_acomodacoes character varying(50),
  tipo_quarto character varying(50),
  CONSTRAINT "PK_quarto" PRIMARY KEY (quarto),
  CONSTRAINT "FK_quarto_hotel" FOREIGN KEY (hotel)
    REFERENCES hoteis (hotel) MATCH SIMPLE
    ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE reservas (
  reserva uuid NOT NULL DEFAULT uuid_generate_V4(),
  quantidade_pessoas smallint,
  data_inicio date NOT NULL,
  data_fim date NOT NULL,
  valor numeric(20,2),
  usuario uuid NOT NULL,
  status character varying(30),
  CONSTRAINT "PK_reserva" PRIMARY KEY (reserva),
  CONSTRAINT "FK_reserva_usuario" FOREIGN KEY (usuario)
    REFERENCES usuarios (usuario) MATCH SIMPLE
    ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE reservas_quartos(
  id uuid NOT NULL DEFAULT uuid_generate_V4(),
  reserva uuid NOT NULL,
  quarto uuid NOT NULL,
  CONSTRAINT "PK_id_reserva_quarto" PRIMARY KEY (id),
  CONSTRAINT "FK_reserva_quartos_reserva" FOREIGN KEY (reserva)
    REFERENCES reservas (reserva) MATCH SIMPLE
    ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT "FK_reserva_quarto_quarto" FOREIGN KEY (quarto)
    REFERENCES quartos (quarto) MATCH SIMPLE
    ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE cancelamentosreservas (
  cancelamentoreserva uuid NOT NULL DEFAULT uuid_generate_V4(),
  reserva uuid NOT NULL,
  motivo TEXT,
  data_cancelamento timestamp without time zone DEFAULT NOW(),
  gerou_nova_reserva boolean,
  CONSTRAINT "PK_cancelamentoreserva" PRIMARY KEY (cancelamentoreserva),
  CONSTRAINT "FK_cancelamentoreserva_reserva" FOREIGN KEY (reserva)
    REFERENCES reservas (reserva) MATCH SIMPLE
    ON UPDATE NO ACTION ON DELETE NO ACTION
);

---INSERTS INICIAIS---

INSERT INTO usuarios (
  usuario, 
  nome,
  cpf_cnpj,
  telefone
) VALUES (
  'ed06c339-0120-4841-bf50-91ec656fffaa',
  'Fulano da Silva',
  '123.456.789-10',
  '21987654321'
),
(
  '82ed85b1-468d-4070-a006-67d8d982e03b',
  'Beltrano de Souza',
  '234.567.891-01',
  '21998765432'
),
(
  '65bb1ba5-4b08-4226-9807-0686b6ac8e60',
  'Ciclano dos Santos',
  '345.678.910-12',
  '21976543210'
);

INSERT INTO hoteis (
  hotel,
  cnpj,
  nome_fantasia,
  razao_social,
  classificacao
) VALUES (
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  '85.876.591/0001-18',
  'Mock Hotel VIP',
  'Hotel Ficticio Mock VIP LTDA',
  'CINCO_ESTRELAS'
),
(
  'fa063e11-d6b9-49c7-b56a-be5d759edf7d',
  '58.729.938/0001-27',
  'Mock Hotel',
  'Hotel Ficticio Mock LTDA',
  'TRES_ESTRELAS'
);

INSERT INTO quartos (
  hotel,
  quantidade_acomodacoes,
  tipo_acomodacoes,
  tipo_quarto  
) VALUES 
--Mock Hotel
(
  'fa063e11-d6b9-49c7-b56a-be5d759edf7d',
  2,
  'CAMA_CASAL',
  'STANDARD_NAO_FUMANTES'
),
(
  'fa063e11-d6b9-49c7-b56a-be5d759edf7d',
  3,
  'CAMAS_CASAL_SOLTEIRO',
  'STANDARD_NAO_FUMANTES'
),
(
  'fa063e11-d6b9-49c7-b56a-be5d759edf7d',
  2,
  'CAMAS_SOLTEIRO',
  'STANDARD_NAO_FUMANTES'
),
(
  'fa063e11-d6b9-49c7-b56a-be5d759edf7d',
  4,
  'CAMAS_CASAL_BELICHE',
  'STANDARD_NAO_FUMANTES'
),
(
  'fa063e11-d6b9-49c7-b56a-be5d759edf7d',
  2,
  'CAMA_CASAL',
  'STANDARD_FUMANTES'
),
(
  'fa063e11-d6b9-49c7-b56a-be5d759edf7d',
  3,
  'CAMAS_CASAL_SOLTEIRO',
  'STANDARD_FUMANTES'
),
(
  'fa063e11-d6b9-49c7-b56a-be5d759edf7d',
  2,
  'CAMAS_SOLTEIRO',
  'STANDARD_FUMANTES'
),
(
  'fa063e11-d6b9-49c7-b56a-be5d759edf7d',
  4,
  'CAMAS_CASAL_BELICHE',
  'STANDARD_FUMANTES'
),
--Mock Hotel VIP
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  2,
  'CAMA_CASAL',
  'STANDARD_NAO_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  3,
  'CAMAS_CASAL_SOLTEIRO',
  'STANDARD_NAO_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  2,
  'CAMAS_SOLTEIRO',
  'STANDARD_NAO_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  4,
  'CAMAS_CASAL_BELICHE',
  'STANDARD_NAO_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  2,
  'CAMA_CASAL',
  'STANDARD_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  3,
  'CAMAS_CASAL_SOLTEIRO',
  'STANDARD_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  2,
  'CAMAS_SOLTEIRO',
  'STANDARD_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  4,
  'CAMAS_CASAL_BELICHE',
  'STANDARD_FUMANTES'
),
--Quartos VIP
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  2,
  'CAMA_CASAL',
  'VIP_NAO_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  3,
  'CAMAS_CASAL_SOLTEIRO',
  'VIP_NAO_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  2,
  'CAMAS_SOLTEIRO',
  'VIP_NAO_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  4,
  'CAMAS_CASAL_BELICHE',
  'VIP_NAO_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  2,
  'CAMA_CASAL',
  'VIP_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  3,
  'CAMAS_CASAL_SOLTEIRO',
  'VIP_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  2,
  'CAMAS_SOLTEIRO',
  'VIP_FUMANTES'
),
(
  '1deb1d1e-d3a0-4fce-9077-f1188cce73b1',
  4,
  'CAMAS_CASAL_BELICHE',
  'VIP_FUMANTES'
);




