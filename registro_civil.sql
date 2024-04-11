PGDMP  1             
        |            Registro_CivilDB    16.2    16.2 *               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                        0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            !           1262    16398    Registro_CivilDB    DATABASE     �   CREATE DATABASE "Registro_CivilDB" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Venezuela.1252';
 "   DROP DATABASE "Registro_CivilDB";
                postgres    false            �            1259    16406 
   Ciudadanos    TABLE     �   CREATE TABLE public."Ciudadanos" (
    cedula integer NOT NULL,
    nacionalidad text NOT NULL,
    estado_civil text NOT NULL,
    nacimientos_id integer
);
     DROP TABLE public."Ciudadanos";
       public         heap    postgres    false            �            1259    16426    Defunciones    TABLE     �   CREATE TABLE public."Defunciones" (
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
       public         heap    postgres    false            �            1259    16507    Matrimonios    TABLE     B  CREATE TABLE public."Matrimonios" (
    id integer NOT NULL,
    contrayente1_cedula integer,
    contrayente2_cedula integer,
    contrayente1_padre1_cedula integer,
    contrayente1_padre2_cedula integer,
    contrayente2_padre1_cedula integer,
    contrayente2_padre2_cedula integer,
    "fecha_ActaMatrimonio" date
);
 !   DROP TABLE public."Matrimonios";
       public         heap    postgres    false            �            1259    16399    Nacimientos    TABLE     x  CREATE TABLE public."Nacimientos" (
    id integer NOT NULL,
    nombre text NOT NULL,
    sexo text NOT NULL,
    fecha_nacimiento date NOT NULL,
    hora_nacimiento time without time zone NOT NULL,
    lugar_nacimiento text NOT NULL,
    padre1_cedula integer,
    padre2_cedula integer,
    testigo1_cedula integer,
    testigo2_cedula integer,
    parroquia_id integer
);
 !   DROP TABLE public."Nacimientos";
       public         heap    postgres    false            �            1259    16458 
   Parroquias    TABLE     t   CREATE TABLE public."Parroquias" (
    id integer NOT NULL,
    nombre text,
    estado text,
    municipio text
);
     DROP TABLE public."Parroquias";
       public         heap    postgres    false            �            1259    16487    Testigos    TABLE     7   CREATE TABLE public."Testigos" (
    cedula integer
);
    DROP TABLE public."Testigos";
       public         heap    postgres    false                      0    16406 
   Ciudadanos 
   TABLE DATA           Z   COPY public."Ciudadanos" (cedula, nacionalidad, estado_civil, nacimientos_id) FROM stdin;
    public          postgres    false    216   &8                 0    16426    Defunciones 
   TABLE DATA           �   COPY public."Defunciones" (cedula, fecha_defuncion, hora_defuncion, lugar_defuncion, destino_cadaver, causa_defuncion) FROM stdin;
    public          postgres    false    217   �8                 0    16542 	   Divorcios 
   TABLE DATA           g   COPY public."Divorcios" (id, divorciado1_cedula, divorciado2_cedula, "fecha_ActaDivorcio") FROM stdin;
    public          postgres    false    221   �8                 0    16507    Matrimonios 
   TABLE DATA           �   COPY public."Matrimonios" (id, contrayente1_cedula, contrayente2_cedula, contrayente1_padre1_cedula, contrayente1_padre2_cedula, contrayente2_padre1_cedula, contrayente2_padre2_cedula, "fecha_ActaMatrimonio") FROM stdin;
    public          postgres    false    220   �8                 0    16399    Nacimientos 
   TABLE DATA           �   COPY public."Nacimientos" (id, nombre, sexo, fecha_nacimiento, hora_nacimiento, lugar_nacimiento, padre1_cedula, padre2_cedula, testigo1_cedula, testigo2_cedula, parroquia_id) FROM stdin;
    public          postgres    false    215   �8                 0    16458 
   Parroquias 
   TABLE DATA           E   COPY public."Parroquias" (id, nombre, estado, municipio) FROM stdin;
    public          postgres    false    218   �9                 0    16487    Testigos 
   TABLE DATA           ,   COPY public."Testigos" (cedula) FROM stdin;
    public          postgres    false    219   �9       j           2606    16692    Ciudadanos Ciudadanos_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public."Ciudadanos"
    ADD CONSTRAINT "Ciudadanos_pkey" PRIMARY KEY (cedula);
 H   ALTER TABLE ONLY public."Ciudadanos" DROP CONSTRAINT "Ciudadanos_pkey";
       public            postgres    false    216            t           2606    16546    Divorcios Divorcios_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public."Divorcios"
    ADD CONSTRAINT "Divorcios_pkey" PRIMARY KEY (id);
 F   ALTER TABLE ONLY public."Divorcios" DROP CONSTRAINT "Divorcios_pkey";
       public            postgres    false    221            r           2606    16511    Matrimonios Matrimonios_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT "Matrimonios_pkey" PRIMARY KEY (id);
 J   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT "Matrimonios_pkey";
       public            postgres    false    220            h           2606    16405    Nacimientos Nacimientos_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."Nacimientos"
    ADD CONSTRAINT "Nacimientos_pkey" PRIMARY KEY (id);
 J   ALTER TABLE ONLY public."Nacimientos" DROP CONSTRAINT "Nacimientos_pkey";
       public            postgres    false    215            n           2606    16464    Parroquias Parroquias_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public."Parroquias"
    ADD CONSTRAINT "Parroquias_pkey" PRIMARY KEY (id);
 H   ALTER TABLE ONLY public."Parroquias" DROP CONSTRAINT "Parroquias_pkey";
       public            postgres    false    218            p           2606    16496    Testigos unique_cedula 
   CONSTRAINT     f   ALTER TABLE ONLY public."Testigos"
    ADD CONSTRAINT unique_cedula UNIQUE (cedula) INCLUDE (cedula);
 B   ALTER TABLE ONLY public."Testigos" DROP CONSTRAINT unique_cedula;
       public            postgres    false    219            l           2606    16437    Ciudadanos uq_cedula 
   CONSTRAINT     S   ALTER TABLE ONLY public."Ciudadanos"
    ADD CONSTRAINT uq_cedula UNIQUE (cedula);
 @   ALTER TABLE ONLY public."Ciudadanos" DROP CONSTRAINT uq_cedula;
       public            postgres    false    216            u           2606    16438 *   Nacimientos Nacimientos_padre1_cedula_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Nacimientos"
    ADD CONSTRAINT "Nacimientos_padre1_cedula_fkey" FOREIGN KEY (padre1_cedula) REFERENCES public."Ciudadanos"(cedula);
 X   ALTER TABLE ONLY public."Nacimientos" DROP CONSTRAINT "Nacimientos_padre1_cedula_fkey";
       public          postgres    false    4716    215    216            {           2606    16431    Defunciones cedula    FK CONSTRAINT     z   ALTER TABLE ONLY public."Defunciones"
    ADD CONSTRAINT cedula FOREIGN KEY (cedula) REFERENCES public."Nacimientos"(id);
 >   ALTER TABLE ONLY public."Defunciones" DROP CONSTRAINT cedula;
       public          postgres    false    217    215    4712            |           2606    16490    Testigos fk_cedula    FK CONSTRAINT     }   ALTER TABLE ONLY public."Testigos"
    ADD CONSTRAINT fk_cedula FOREIGN KEY (cedula) REFERENCES public."Ciudadanos"(cedula);
 >   ALTER TABLE ONLY public."Testigos" DROP CONSTRAINT fk_cedula;
       public          postgres    false    219    4716    216            }           2606    16512    Matrimonios fk_contrayente1    FK CONSTRAINT     �   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT fk_contrayente1 FOREIGN KEY (contrayente1_cedula) REFERENCES public."Ciudadanos"(cedula);
 G   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT fk_contrayente1;
       public          postgres    false    216    4716    220            ~           2606    16522 "   Matrimonios fk_contrayente1_padre1    FK CONSTRAINT     �   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT fk_contrayente1_padre1 FOREIGN KEY (contrayente1_padre1_cedula) REFERENCES public."Ciudadanos"(cedula);
 N   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT fk_contrayente1_padre1;
       public          postgres    false    4716    220    216                       2606    16527 "   Matrimonios fk_contrayente1_padre2    FK CONSTRAINT     �   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT fk_contrayente1_padre2 FOREIGN KEY (contrayente1_padre2_cedula) REFERENCES public."Ciudadanos"(cedula);
 N   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT fk_contrayente1_padre2;
       public          postgres    false    220    4716    216            �           2606    16517    Matrimonios fk_contrayente2    FK CONSTRAINT     �   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT fk_contrayente2 FOREIGN KEY (contrayente2_cedula) REFERENCES public."Ciudadanos"(cedula);
 G   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT fk_contrayente2;
       public          postgres    false    4716    220    216            �           2606    16532 "   Matrimonios fk_contrayente2_padre1    FK CONSTRAINT     �   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT fk_contrayente2_padre1 FOREIGN KEY (contrayente2_padre1_cedula) REFERENCES public."Ciudadanos"(cedula);
 N   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT fk_contrayente2_padre1;
       public          postgres    false    216    4716    220            �           2606    16537 "   Matrimonios fk_contrayente2_padre2    FK CONSTRAINT     �   ALTER TABLE ONLY public."Matrimonios"
    ADD CONSTRAINT fk_contrayente2_padre2 FOREIGN KEY (contrayente2_padre2_cedula) REFERENCES public."Ciudadanos"(cedula);
 N   ALTER TABLE ONLY public."Matrimonios" DROP CONSTRAINT fk_contrayente2_padre2;
       public          postgres    false    216    4716    220            �           2606    16547    Divorcios fk_divorciado1    FK CONSTRAINT     �   ALTER TABLE ONLY public."Divorcios"
    ADD CONSTRAINT fk_divorciado1 FOREIGN KEY (divorciado1_cedula) REFERENCES public."Ciudadanos"(cedula);
 D   ALTER TABLE ONLY public."Divorcios" DROP CONSTRAINT fk_divorciado1;
       public          postgres    false    221    216    4716            �           2606    16552    Divorcios fk_divorciado2    FK CONSTRAINT     �   ALTER TABLE ONLY public."Divorcios"
    ADD CONSTRAINT fk_divorciado2 FOREIGN KEY (divorciado2_cedula) REFERENCES public."Ciudadanos"(cedula);
 D   ALTER TABLE ONLY public."Divorcios" DROP CONSTRAINT fk_divorciado2;
       public          postgres    false    216    221    4716            �           2606    16557    Divorcios fk_id    FK CONSTRAINT     }   ALTER TABLE ONLY public."Divorcios"
    ADD CONSTRAINT fk_id FOREIGN KEY (id) REFERENCES public."Matrimonios"(id) NOT VALID;
 ;   ALTER TABLE ONLY public."Divorcios" DROP CONSTRAINT fk_id;
       public          postgres    false    4722    220    221            v           2606    16467    Nacimientos fk_padre2_cedula    FK CONSTRAINT     �   ALTER TABLE ONLY public."Nacimientos"
    ADD CONSTRAINT fk_padre2_cedula FOREIGN KEY (padre2_cedula) REFERENCES public."Ciudadanos"(cedula);
 H   ALTER TABLE ONLY public."Nacimientos" DROP CONSTRAINT fk_padre2_cedula;
       public          postgres    false    216    215    4716            w           2606    16482    Nacimientos fk_parroquia_id    FK CONSTRAINT     �   ALTER TABLE ONLY public."Nacimientos"
    ADD CONSTRAINT fk_parroquia_id FOREIGN KEY (parroquia_id) REFERENCES public."Parroquias"(id);
 G   ALTER TABLE ONLY public."Nacimientos" DROP CONSTRAINT fk_parroquia_id;
       public          postgres    false    218    215    4718            x           2606    16497    Nacimientos fk_testigo1_cedula    FK CONSTRAINT     �   ALTER TABLE ONLY public."Nacimientos"
    ADD CONSTRAINT fk_testigo1_cedula FOREIGN KEY (testigo1_cedula) REFERENCES public."Testigos"(cedula) NOT VALID;
 J   ALTER TABLE ONLY public."Nacimientos" DROP CONSTRAINT fk_testigo1_cedula;
       public          postgres    false    215    219    4720            y           2606    16502    Nacimientos fk_testigo2_cedula    FK CONSTRAINT     �   ALTER TABLE ONLY public."Nacimientos"
    ADD CONSTRAINT fk_testigo2_cedula FOREIGN KEY (testigo2_cedula) REFERENCES public."Testigos"(cedula) NOT VALID;
 J   ALTER TABLE ONLY public."Nacimientos" DROP CONSTRAINT fk_testigo2_cedula;
       public          postgres    false    215    4720    219            z           2606    16693    Ciudadanos id_nacimientos_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public."Ciudadanos"
    ADD CONSTRAINT id_nacimientos_fk FOREIGN KEY (nacimientos_id) REFERENCES public."Nacimientos"(id) NOT VALID;
 H   ALTER TABLE ONLY public."Ciudadanos" DROP CONSTRAINT id_nacimientos_fk;
       public          postgres    false    216    4712    215               R   x�36026�04�K�K���I�����)I-��4�27�45�0BH&r�d��%g&�$rs�YZ�!k���sq��qqq ˿i            x������ � �            x������ � �         -   x�3�47�45�0�47��005��C #C]]#�=... ѣ�         �   x�e�M
�0�����@%��ָ+�?�t3�YD�-��ENo�
���p(tz�����^Ɣ8�ލ�gN���0�+��)34��ژi����)Bs�������zHx�u���L"�����3;i�I�B��~=�#��1��*�W��TZc�J�ЁqnU�W*�V����f��z-�J�         *   x�3�t�/,�,KL�O�*��L��M,JLN�L������ �Z
�            x������ � �     