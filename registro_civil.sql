PGDMP      (                |            Registro_CivilDB    16.2    16.2 (               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16398    Registro_CivilDB    DATABASE     �   CREATE DATABASE "Registro_CivilDB" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Venezuela.1252';
 "   DROP DATABASE "Registro_CivilDB";
                postgres    false            �            1259    16956    ciudadanos_cedula_seq    SEQUENCE     ~   CREATE SEQUENCE public.ciudadanos_cedula_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.ciudadanos_cedula_seq;
       public          postgres    false            �            1259    16406 
   Ciudadanos    TABLE     �   CREATE TABLE public."Ciudadanos" (
    cedula integer DEFAULT nextval('public.ciudadanos_cedula_seq'::regclass) NOT NULL,
    nacionalidad text NOT NULL,
    estado_civil text NOT NULL,
    nacimientos_id integer NOT NULL
);
     DROP TABLE public."Ciudadanos";
       public         heap    postgres    false    221            �            1259    16426    Defunciones    TABLE     �   CREATE TABLE public."Defunciones" (
    cedula integer,
    fecha_defuncion date NOT NULL,
    hora_defuncion time without time zone NOT NULL,
    lugar_defuncion text,
    destino_cadaver text,
    causa_defuncion text
);
 !   DROP TABLE public."Defunciones";
       public         heap    postgres    false            �            1259    16542 	   Divorcios    TABLE     �   CREATE TABLE public."Divorcios" (
    id integer NOT NULL,
    divorciado1_cedula integer,
    divorciado2_cedula integer,
    "fecha_ActaDivorcio" date
);
    DROP TABLE public."Divorcios";
       public         heap    postgres    false            �            1259    17184    matrimonios_id_seq    SEQUENCE     {   CREATE SEQUENCE public.matrimonios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.matrimonios_id_seq;
       public          postgres    false            �            1259    16507    Matrimonios    TABLE     y  CREATE TABLE public."Matrimonios" (
    id integer DEFAULT nextval('public.matrimonios_id_seq'::regclass) NOT NULL,
    contrayente1_cedula integer,
    contrayente2_cedula integer,
    contrayente1_padre1_cedula integer,
    contrayente1_padre2_cedula integer,
    contrayente2_padre1_cedula integer,
    contrayente2_padre2_cedula integer,
    "fecha_ActaMatrimonio" date
);
 !   DROP TABLE public."Matrimonios";
       public         heap    postgres    false    222            �            1259    16954    nacimientos_id_seq    SEQUENCE     {   CREATE SEQUENCE public.nacimientos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.nacimientos_id_seq;
       public          postgres    false            �            1259    16399    Nacimientos    TABLE     �  CREATE TABLE public."Nacimientos" (
    id integer DEFAULT nextval('public.nacimientos_id_seq'::regclass) NOT NULL,
    nombre text NOT NULL,
    sexo text NOT NULL,
    fecha_nacimiento date NOT NULL,
    hora_nacimiento time without time zone NOT NULL,
    lugar_nacimiento text NOT NULL,
    padre1_cedula integer,
    padre2_cedula integer,
    testigo1_cedula integer,
    testigo2_cedula integer,
    parroquia text
);
 !   DROP TABLE public."Nacimientos";
       public         heap    postgres    false    220                      0    16406 
   Ciudadanos 
   TABLE DATA           Z   COPY public."Ciudadanos" (cedula, nacionalidad, estado_civil, nacimientos_id) FROM stdin;
    public          postgres    false    216   u8                 0    16426    Defunciones 
   TABLE DATA           �   COPY public."Defunciones" (cedula, fecha_defuncion, hora_defuncion, lugar_defuncion, destino_cadaver, causa_defuncion) FROM stdin;
    public          postgres    false    217   �8                 0    16542 	   Divorcios 
   TABLE DATA           g   COPY public."Divorcios" (id, divorciado1_cedula, divorciado2_cedula, "fecha_ActaDivorcio") FROM stdin;
    public          postgres    false    219   \9                 0    16507    Matrimonios 
   TABLE DATA           �   COPY public."Matrimonios" (id, contrayente1_cedula, contrayente2_cedula, contrayente1_padre1_cedula, contrayente1_padre2_cedula, contrayente2_padre1_cedula, contrayente2_padre2_cedula, "fecha_ActaMatrimonio") FROM stdin;
    public          postgres    false    218   y9                 0    16399    Nacimientos 
   TABLE DATA           �   COPY public."Nacimientos" (id, nombre, sexo, fecha_nacimiento, hora_nacimiento, lugar_nacimiento, padre1_cedula, padre2_cedula, testigo1_cedula, testigo2_cedula, parroquia) FROM stdin;
    public          postgres    false    215   �9                  0    0    ciudadanos_cedula_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.ciudadanos_cedula_seq', 2, true);
          public          postgres    false    221                       0    0    matrimonios_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.matrimonios_id_seq', 1, false);
          public          postgres    false    222                       0    0    nacimientos_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.nacimientos_id_seq', 4, true);
          public          postgres    false    220            h           2606    16692    Ciudadanos Ciudadanos_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public."Ciudadanos"
    ADD CONSTRAINT "Ciudadanos_pkey" PRIMARY KEY (cedula);
 H   ALTER TABLE ONLY public."Ciudadanos" DROP CONSTRAINT "Ciudadanos_pkey";
       public            postgres    false    216            n           2606    16546    Divorcios Divorcios_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public."Divorcios"
    ADD CONSTRAINT "Divorcios_pkey" PRIMARY KEY (id);
 F   ALTER TABLE ONLY public."Divorcios" DROP CONSTRAINT "Divorcios_pkey";
       public            postgres    false    219            l           2606    16511    Matrimonios Matrimonios_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT "Matrimonios_pkey" PRIMARY KEY (id);
 J   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT "Matrimonios_pkey";
       public            postgres    false    218            f           2606    16925    Nacimientos Nacimientos_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."Nacimientos"
    ADD CONSTRAINT "Nacimientos_pkey" PRIMARY KEY (id);
 J   ALTER TABLE ONLY public."Nacimientos" DROP CONSTRAINT "Nacimientos_pkey";
       public            postgres    false    215            j           2606    16437    Ciudadanos uq_cedula 
   CONSTRAINT     S   ALTER TABLE ONLY public."Ciudadanos"
    ADD CONSTRAINT uq_cedula UNIQUE (cedula);
 @   ALTER TABLE ONLY public."Ciudadanos" DROP CONSTRAINT uq_cedula;
       public            postgres    false    216            t           2606    16856    Defunciones cedula    FK CONSTRAINT     �   ALTER TABLE ONLY public."Defunciones"
    ADD CONSTRAINT cedula FOREIGN KEY (cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 >   ALTER TABLE ONLY public."Defunciones" DROP CONSTRAINT cedula;
       public          postgres    false    4714    217    216            u           2606    16876    Matrimonios fk_contrayente1    FK CONSTRAINT     �   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT fk_contrayente1 FOREIGN KEY (contrayente1_cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 G   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT fk_contrayente1;
       public          postgres    false    216    218    4714            v           2606    16886 "   Matrimonios fk_contrayente1_padre1    FK CONSTRAINT     �   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT fk_contrayente1_padre1 FOREIGN KEY (contrayente1_padre1_cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 N   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT fk_contrayente1_padre1;
       public          postgres    false    216    218    4714            w           2606    16891 "   Matrimonios fk_contrayente1_padre2    FK CONSTRAINT     �   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT fk_contrayente1_padre2 FOREIGN KEY (contrayente1_padre2_cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 N   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT fk_contrayente1_padre2;
       public          postgres    false    218    216    4714            x           2606    16881    Matrimonios fk_contrayente2    FK CONSTRAINT     �   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT fk_contrayente2 FOREIGN KEY (contrayente2_cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 G   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT fk_contrayente2;
       public          postgres    false    218    4714    216            y           2606    16896 "   Matrimonios fk_contrayente2_padre1    FK CONSTRAINT     �   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT fk_contrayente2_padre1 FOREIGN KEY (contrayente2_padre1_cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 N   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT fk_contrayente2_padre1;
       public          postgres    false    216    218    4714            z           2606    16901 "   Matrimonios fk_contrayente2_padre2    FK CONSTRAINT     �   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT fk_contrayente2_padre2 FOREIGN KEY (contrayente2_padre2_cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 N   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT fk_contrayente2_padre2;
       public          postgres    false    4714    216    218            {           2606    16861    Divorcios fk_divorciado1    FK CONSTRAINT     �   ALTER TABLE ONLY public."Divorcios"
    ADD CONSTRAINT fk_divorciado1 FOREIGN KEY (divorciado1_cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 D   ALTER TABLE ONLY public."Divorcios" DROP CONSTRAINT fk_divorciado1;
       public          postgres    false    4714    219    216            |           2606    16866    Divorcios fk_divorciado2    FK CONSTRAINT     �   ALTER TABLE ONLY public."Divorcios"
    ADD CONSTRAINT fk_divorciado2 FOREIGN KEY (divorciado2_cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 D   ALTER TABLE ONLY public."Divorcios" DROP CONSTRAINT fk_divorciado2;
       public          postgres    false    219    4714    216            }           2606    16871    Divorcios fk_id    FK CONSTRAINT     �   ALTER TABLE ONLY public."Divorcios"
    ADD CONSTRAINT fk_id FOREIGN KEY (id) REFERENCES public."Matrimonios"(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 ;   ALTER TABLE ONLY public."Divorcios" DROP CONSTRAINT fk_id;
       public          postgres    false    219    218    4716            o           2606    16831    Nacimientos fk_padre1_cedula    FK CONSTRAINT     �   ALTER TABLE ONLY public."Nacimientos"
    ADD CONSTRAINT fk_padre1_cedula FOREIGN KEY (padre1_cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 H   ALTER TABLE ONLY public."Nacimientos" DROP CONSTRAINT fk_padre1_cedula;
       public          postgres    false    216    4714    215            p           2606    16836    Nacimientos fk_padre2_cedula    FK CONSTRAINT     �   ALTER TABLE ONLY public."Nacimientos"
    ADD CONSTRAINT fk_padre2_cedula FOREIGN KEY (padre2_cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 H   ALTER TABLE ONLY public."Nacimientos" DROP CONSTRAINT fk_padre2_cedula;
       public          postgres    false    216    215    4714            q           2606    16841    Nacimientos fk_testigo1_cedula    FK CONSTRAINT     �   ALTER TABLE ONLY public."Nacimientos"
    ADD CONSTRAINT fk_testigo1_cedula FOREIGN KEY (testigo1_cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 J   ALTER TABLE ONLY public."Nacimientos" DROP CONSTRAINT fk_testigo1_cedula;
       public          postgres    false    216    4714    215            r           2606    16846    Nacimientos fk_testigo2_cedula    FK CONSTRAINT     �   ALTER TABLE ONLY public."Nacimientos"
    ADD CONSTRAINT fk_testigo2_cedula FOREIGN KEY (testigo2_cedula) REFERENCES public."Ciudadanos"(cedula) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 J   ALTER TABLE ONLY public."Nacimientos" DROP CONSTRAINT fk_testigo2_cedula;
       public          postgres    false    216    215    4714            s           2606    16926    Ciudadanos id_nacimientos_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public."Ciudadanos"
    ADD CONSTRAINT id_nacimientos_fk FOREIGN KEY (nacimientos_id) REFERENCES public."Nacimientos"(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 H   ALTER TABLE ONLY public."Ciudadanos" DROP CONSTRAINT id_nacimientos_fk;
       public          postgres    false    4710    216    215               `   x�]�;
�0 �99�'���N���l!4�����c���RV��II�I������0�����\�#*���ƙ�U��)D�/�*���{���^!�         g   x��1�0��9�/ r�S/�ҡCY*�4�!R�Q�������4Ƞ�hwIƻ���}��̞r���S\���1�iB�g��pd����n�Q8���҇��	�            x������ � �            x������ � �         �   x�u��
�0��s�{�I��8{�Q| /YW��5�m���SP�%���p�f8pSFf*E�J	X�2�p�H�|�p�̳�G�d�D'��.}�48��'N���:t���4�~�ۻ����|YHJ���#H��N6�
�s����W<�PYL��u4~��R�FIC5�*r�ɨtnLm�m!�xE+U�     