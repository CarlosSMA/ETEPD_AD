CREATE TABLE "paciente" (
	"codigo" bigint NOT NULL DEFAULT '0',
	"nome" varchar,
	"email" varchar,
	"celular" varchar,
	"data_nascimento" date,
	"cpf" varchar,
	"rg" varchar,
	"logadouro" varchar,
	"complemento" varchar,
	PRIMARY KEY ("codigo")
);

CREATE TABLE "agenda" (
	"codigo" bigint NOT NULL DEFAULT '0',
	"nome_dentista" varchar,
	"nome_paciente" varchar,
	"plano" varchar,
	"concluido" bit,
	"cancelado" bit,
	"reagendado" bit,
	PRIMARY KEY ("codigo")
);

CREATE TABLE "login" (
	"codigo" bigint NOT NULL DEFAULT '0',
	"usuario" varchar,
	"senha" varchar,
	"tipo_usuario" bit,
	PRIMARY KEY ("codigo")
);

CREATE TABLE "dentista" (
	"codigo" bigint NOT NULL DEFAULT '0',
	"cro" varchar,
	"nome" varchar,
	"email" varchar,
	"celular" varchar,
	"data_nascimento" date,
	"cpf" varchar,
	"rg" varchar,
	"logadouro" varchar,
	"complemento" varchar,
	PRIMARY KEY ("codigo")
);

CREATE TABLE "odontograma" (
	"operacao" bigint NOT NULL DEFAULT '0',
	"codigo" int,
	"plano" int,
	"data" date,
	"descricao" varchar,
	"observacao" varchar,
	PRIMARY KEY ("operacao")
);

ALTER TABLE "agenda" ADD FOREIGN KEY ("codigo") REFERENCES "login" ("codigo");

ALTER TABLE "paciente" ADD FOREIGN KEY ("codigo") REFERENCES "login" ("codigo");

ALTER TABLE "odontograma" ADD FOREIGN KEY ("operacao") REFERENCES "login" ("codigo");

ALTER TABLE "dentista" ADD FOREIGN KEY ("codigo") REFERENCES "login" ("codigo");

ALTER TABLE "agenda" ADD FOREIGN KEY ("codigo") REFERENCES "dentista" ("codigo");

ALTER TABLE "odontograma" ADD FOREIGN KEY ("operacao") REFERENCES "agenda" ("codigo");

ALTER TABLE "odontograma" ADD FOREIGN KEY ("operacao") REFERENCES "dentista" ("codigo");

ALTER TABLE "odontograma" ADD FOREIGN KEY ("operacao") REFERENCES "paciente" ("codigo");
