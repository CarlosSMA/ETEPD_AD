CREATE TABLE "paciente" (
  "codigo" SERIAL PRIMARY KEY,
  "nome" varchar,
  "email" varchar,
  "celular" varchar,
  "data_nascimento" date,
  "cpf" varchar,
  "rg" varchar,
  "logadouro" varchar,
  "complemento" varchar
);

CREATE TABLE "agenda" (
  "codigo" int PRIMARY KEY,
  "nome_dentista" varchar,
  "nome_paciente" varchar,
  "plano" varchar,
  "concluido" bit,
  "cancelado" bit,
  "reagendado" bit
);

CREATE TABLE "login" (
  "codigo" int PRIMARY KEY,
  "usuario" varchar,
  "senha" varchar,
  "tipo_usuario" bit
);

CREATE TABLE "dentista" (
  "codigo" int PRIMARY KEY,
  "cro" varchar,
  "nome" varchar,
  "email" varchar,
  "celular" varchar,
  "data_nascimento" date,
  "cpf" varchar,
  "rg" varchar,
  "logadouro" varchar,
  "complemento" varchar
);

CREATE TABLE "odontograma" (
  "operacao" varchar PRIMARY KEY,
  "codigo" int,
  "plano" int,
  "data" date,
  "descricao" varchar,
  "observacao" varchar
);

ALTER TABLE "agenda" ADD FOREIGN KEY ("codigo") REFERENCES "login" ("codigo");

ALTER TABLE "paciente" ADD FOREIGN KEY ("codigo") REFERENCES "login" ("codigo");

ALTER TABLE "odontograma" ADD FOREIGN KEY ("operacao") REFERENCES "login" ("codigo");

ALTER TABLE "dentista" ADD FOREIGN KEY ("codigo") REFERENCES "login" ("codigo");

ALTER TABLE "agenda" ADD FOREIGN KEY ("codigo") REFERENCES "dentista" ("codigo");

ALTER TABLE "odontograma" ADD FOREIGN KEY ("operacao") REFERENCES "agenda" ("codigo");

ALTER TABLE "odontograma" ADD FOREIGN KEY ("operacao") REFERENCES "dentista" ("codigo");

ALTER TABLE "odontograma" ADD FOREIGN KEY ("operacao") REFERENCES "paciente" ("codigo");
