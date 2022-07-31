--
-- PostgreSQL database dump
--

-- Dumped from database version 13.6
-- Dumped by pg_dump version 13.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: cidade; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cidade (
    id integer NOT NULL,
    sigla character varying(256) NOT NULL,
    nome character varying(256) NOT NULL
);


ALTER TABLE public.cidade OWNER TO postgres;

--
-- Name: cidade_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cidade_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cidade_id_seq OWNER TO postgres;

--
-- Name: cidade_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cidade_id_seq OWNED BY public.cidade.id;


--
-- Name: cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente (
    id integer NOT NULL,
    cpf character varying(256) NOT NULL,
    nome character varying(256) NOT NULL,
    data_nascimento character varying(256) NOT NULL,
    endereco_id integer
);


ALTER TABLE public.cliente OWNER TO postgres;

--
-- Name: cliente_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cliente_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cliente_id_seq OWNER TO postgres;

--
-- Name: cliente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cliente_id_seq OWNED BY public.cliente.id;


--
-- Name: editora; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.editora (
    id integer NOT NULL,
    nome character varying(256) NOT NULL
);


ALTER TABLE public.editora OWNER TO postgres;

--
-- Name: editora_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.editora_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.editora_id_seq OWNER TO postgres;

--
-- Name: editora_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.editora_id_seq OWNED BY public.editora.id;


--
-- Name: endereco; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.endereco (
    id integer NOT NULL,
    cep character varying(256) NOT NULL,
    logradouro character varying(256) NOT NULL,
    numero integer NOT NULL,
    complemento character varying(256) NOT NULL,
    cidade_id integer,
    estado_id integer,
    pais_id integer
);


ALTER TABLE public.endereco OWNER TO postgres;

--
-- Name: endereco_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.endereco_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.endereco_id_seq OWNER TO postgres;

--
-- Name: endereco_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.endereco_id_seq OWNED BY public.endereco.id;


--
-- Name: estado; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estado (
    id integer NOT NULL,
    sigla character varying(256) NOT NULL,
    nome character varying(256) NOT NULL
);


ALTER TABLE public.estado OWNER TO postgres;

--
-- Name: estado_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.estado_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.estado_id_seq OWNER TO postgres;

--
-- Name: estado_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.estado_id_seq OWNED BY public.estado.id;


--
-- Name: livraria_livro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livraria_livro (
    id integer NOT NULL,
    livraria_id integer,
    livro_id integer,
    quantidade_estoque integer NOT NULL,
    valor double precision NOT NULL,
    prazo_entrega character varying(256) NOT NULL
);


ALTER TABLE public.livraria_livro OWNER TO postgres;

--
-- Name: livraria_livro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.livraria_livro_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.livraria_livro_id_seq OWNER TO postgres;

--
-- Name: livraria_livro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.livraria_livro_id_seq OWNED BY public.livraria_livro.id;


--
-- Name: livrarias; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livrarias (
    id integer NOT NULL,
    nome character varying(256) NOT NULL
);


ALTER TABLE public.livrarias OWNER TO postgres;

--
-- Name: livrarias_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.livrarias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.livrarias_id_seq OWNER TO postgres;

--
-- Name: livrarias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.livrarias_id_seq OWNED BY public.livrarias.id;


--
-- Name: livro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livro (
    id integer NOT NULL,
    titulo character varying(256) NOT NULL,
    ano integer NOT NULL,
    nome_autor character varying(256) NOT NULL,
    isbn character varying(256) NOT NULL,
    editora_id integer,
    assunto character varying(256) NOT NULL
);


ALTER TABLE public.livro OWNER TO postgres;

--
-- Name: livro_cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livro_cliente (
    id integer NOT NULL,
    cliente_id integer,
    livro_id integer
);


ALTER TABLE public.livro_cliente OWNER TO postgres;

--
-- Name: livro_cliente_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.livro_cliente_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.livro_cliente_id_seq OWNER TO postgres;

--
-- Name: livro_cliente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.livro_cliente_id_seq OWNED BY public.livro_cliente.id;


--
-- Name: livro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.livro_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.livro_id_seq OWNER TO postgres;

--
-- Name: livro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.livro_id_seq OWNED BY public.livro.id;


--
-- Name: pais; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pais (
    id integer NOT NULL,
    sigla character varying(256) NOT NULL,
    nome character varying(256) NOT NULL
);


ALTER TABLE public.pais OWNER TO postgres;

--
-- Name: pais_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pais_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pais_id_seq OWNER TO postgres;

--
-- Name: pais_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pais_id_seq OWNED BY public.pais.id;


--
-- Name: cidade id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cidade ALTER COLUMN id SET DEFAULT nextval('public.cidade_id_seq'::regclass);


--
-- Name: cliente id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente ALTER COLUMN id SET DEFAULT nextval('public.cliente_id_seq'::regclass);


--
-- Name: editora id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.editora ALTER COLUMN id SET DEFAULT nextval('public.editora_id_seq'::regclass);


--
-- Name: endereco id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco ALTER COLUMN id SET DEFAULT nextval('public.endereco_id_seq'::regclass);


--
-- Name: estado id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estado ALTER COLUMN id SET DEFAULT nextval('public.estado_id_seq'::regclass);


--
-- Name: livraria_livro id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livraria_livro ALTER COLUMN id SET DEFAULT nextval('public.livraria_livro_id_seq'::regclass);


--
-- Name: livrarias id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livrarias ALTER COLUMN id SET DEFAULT nextval('public.livrarias_id_seq'::regclass);


--
-- Name: livro id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro ALTER COLUMN id SET DEFAULT nextval('public.livro_id_seq'::regclass);


--
-- Name: livro_cliente id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro_cliente ALTER COLUMN id SET DEFAULT nextval('public.livro_cliente_id_seq'::regclass);


--
-- Name: pais id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pais ALTER COLUMN id SET DEFAULT nextval('public.pais_id_seq'::regclass);


--
-- Data for Name: cidade; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.cidade VALUES (1, 'RJ', 'Rio de Janeiro');
INSERT INTO public.cidade VALUES (2, 'SP', 'São Paulo');


--
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.cliente VALUES (2, '111.222.333-00', 'Thor Odinson', '964 a.C.–965 a.C.', 1);


--
-- Data for Name: editora; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.editora VALUES (1, 'Editora FTD');
INSERT INTO public.editora VALUES (2, 'Editora Rocco');
INSERT INTO public.editora VALUES (3, 'Novatec Editora');
INSERT INTO public.editora VALUES (4, 'Darkside Books');


--
-- Data for Name: endereco; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.endereco VALUES (1, '01311-930', 'Avenida Paulista', 1765, 'Sala 1105', 2, 2, 1);


--
-- Data for Name: estado; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.estado VALUES (1, 'RJ', 'Rio de Janeiro');
INSERT INTO public.estado VALUES (2, 'SP', 'São Paulo');


--
-- Data for Name: livraria_livro; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.livraria_livro VALUES (2, 1, 1, 10, 59.89, '10 dias úteis');
INSERT INTO public.livraria_livro VALUES (3, 2, 2, 30, 46.47, '07 dias úteis');
INSERT INTO public.livraria_livro VALUES (4, 2, 1, 17, 50.99, '07 dias úteis');
INSERT INTO public.livraria_livro VALUES (5, 1, 3, 40, 50.99, '15 dias úteis');
INSERT INTO public.livraria_livro VALUES (6, 3, 1, 10, 39.99, '05 dias úteis');
INSERT INTO public.livraria_livro VALUES (7, 3, 3, 21, 49.99, '15 dias úteis');
INSERT INTO public.livraria_livro VALUES (8, 3, 4, 6, 59.99, '10 dias úteis');
INSERT INTO public.livraria_livro VALUES (9, 3, 5, 2, 63.99, '10 dias úteis');


--
-- Data for Name: livrarias; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.livrarias VALUES (1, 'Saraiva');
INSERT INTO public.livrarias VALUES (2, 'Livraria da Travessa');
INSERT INTO public.livrarias VALUES (3, 'Coffee & Books');
INSERT INTO public.livrarias VALUES (4, 'StarBooks');


--
-- Data for Name: livro; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.livro VALUES (1, 'Harry Potter - E a Pedra Filosofal', 2000, 'J. K. Rowling', '978-8532523051', 2, 'Ficção');
INSERT INTO public.livro VALUES (2, 'Web Services RESTful: Aprenda a Criar web Services RESTful em Java na Nuvem do Google', 2015, 'Ricardo R. Lecheta', '978-8575224540', 3, 'Tecnologia');
INSERT INTO public.livro VALUES (3, 'Ed & Lorraine Warren - Demonologistas: Arquivos Sobrenaturais', 2016, 'Gerald Brittle', '978-8594540164', 4, 'Terror');
INSERT INTO public.livro VALUES (4, 'Ed & Lorraine Warren: Lugar Sombrio', 2017, 'Carmen Reed', '978-8594540430', 4, 'Terror');
INSERT INTO public.livro VALUES (5, 'Ed & Lorraine Warren: Vidas Eternas', 2019, 'Robert Curran', '978-8594541680', 4, 'Terror');


--
-- Data for Name: livro_cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: pais; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pais VALUES (1, 'BR', 'Brasil');


--
-- Name: cidade_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cidade_id_seq', 2, true);


--
-- Name: cliente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cliente_id_seq', 2, true);


--
-- Name: editora_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.editora_id_seq', 4, true);


--
-- Name: endereco_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.endereco_id_seq', 1, true);


--
-- Name: estado_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.estado_id_seq', 2, true);


--
-- Name: livraria_livro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.livraria_livro_id_seq', 9, true);


--
-- Name: livrarias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.livrarias_id_seq', 4, true);


--
-- Name: livro_cliente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.livro_cliente_id_seq', 1, false);


--
-- Name: livro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.livro_id_seq', 5, true);


--
-- Name: pais_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pais_id_seq', 1, true);


--
-- Name: cidade cidade_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cidade
    ADD CONSTRAINT cidade_pkey PRIMARY KEY (id);


--
-- Name: cliente cliente_cpf_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_cpf_key UNIQUE (cpf);


--
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (id);


--
-- Name: editora editora_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.editora
    ADD CONSTRAINT editora_pkey PRIMARY KEY (id);


--
-- Name: endereco endereco_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco
    ADD CONSTRAINT endereco_pkey PRIMARY KEY (id);


--
-- Name: estado estado_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estado
    ADD CONSTRAINT estado_pkey PRIMARY KEY (id);


--
-- Name: livraria_livro livraria_livro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livraria_livro
    ADD CONSTRAINT livraria_livro_pkey PRIMARY KEY (id);


--
-- Name: livrarias livrarias_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livrarias
    ADD CONSTRAINT livrarias_pkey PRIMARY KEY (id);


--
-- Name: livro_cliente livro_cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro_cliente
    ADD CONSTRAINT livro_cliente_pkey PRIMARY KEY (id);


--
-- Name: livro livro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro
    ADD CONSTRAINT livro_pkey PRIMARY KEY (id);


--
-- Name: pais pais_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pais
    ADD CONSTRAINT pais_pkey PRIMARY KEY (id);


--
-- Name: cliente cliente_endereco_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_endereco_id_fkey FOREIGN KEY (endereco_id) REFERENCES public.endereco(id);


--
-- Name: endereco endereco_cidade_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco
    ADD CONSTRAINT endereco_cidade_id_fkey FOREIGN KEY (cidade_id) REFERENCES public.cidade(id);


--
-- Name: endereco endereco_estado_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco
    ADD CONSTRAINT endereco_estado_id_fkey FOREIGN KEY (estado_id) REFERENCES public.estado(id);


--
-- Name: endereco endereco_pais_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco
    ADD CONSTRAINT endereco_pais_id_fkey FOREIGN KEY (pais_id) REFERENCES public.pais(id);


--
-- Name: livraria_livro livraria_livro_livraria_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livraria_livro
    ADD CONSTRAINT livraria_livro_livraria_id_fkey FOREIGN KEY (livraria_id) REFERENCES public.livrarias(id);


--
-- Name: livraria_livro livraria_livro_livro_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livraria_livro
    ADD CONSTRAINT livraria_livro_livro_id_fkey FOREIGN KEY (livro_id) REFERENCES public.livro(id);


--
-- Name: livro_cliente livro_cliente_cliente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro_cliente
    ADD CONSTRAINT livro_cliente_cliente_id_fkey FOREIGN KEY (cliente_id) REFERENCES public.cliente(id);


--
-- Name: livro_cliente livro_cliente_livro_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro_cliente
    ADD CONSTRAINT livro_cliente_livro_id_fkey FOREIGN KEY (livro_id) REFERENCES public.livro(id);


--
-- Name: livro livro_editora_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro
    ADD CONSTRAINT livro_editora_id_fkey FOREIGN KEY (editora_id) REFERENCES public.editora(id);


--
-- PostgreSQL database dump complete
--

