# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError
#Modelo Deporte
class Deporte(models.Model):
  _name = 'cdpelotas3763_y.deportes'
  _rec_name='nombre_deporte'
  nombre_deporte = fields.Char(string="Nombre del Deporte")
  instalaciones_asociadas=fields.One2many('cdpelotas3763_y.instalaciones',
     'deporte_asociado',
     string="Instalaciones Asociadas"
  )
#Modelo Socio
class Socio(models.Model):
 _name = 'cdpelotas3763_y.socios'
 _rec_name="nombre"
 _sql_constraints = [
   ('nom_socio_id',
   'UNIQUE (num_socio)',
   'Ya existe un numero de socio con ese id')]
 num_socio = fields.Integer(string="Numero de socio")
 nombre = fields.Char(string="Nombre")
 apellidos = fields.Char(string="Apellidos")
 direccion = fields.Char(string="Direccion")
 telefono = fields.Integer(string="Teléfono")
 fecha_alta = fields.Date(string="Fecha de Alta")
 reservas_realizadas=fields.One2many('cdpelotas3763_y.reservas',
     'socio',
     string="Reservas Realizadas"
  )
 #Modelo Instalaciones
class Instalaciones(models.Model):
 _name = 'cdpelotas3763_y.instalaciones'
 _rec_name="nombre_pista"
 _sql_constraints = [
        ('num_pista_id',
         'UNIQUE (num_pista)',
         'Ya existe un numero de pista con ese id')]
 num_pista = fields.Integer(string="Numero de pista")
 nombre_pista = fields.Char(string="Nombre de Pista")
 superficie = fields.Selection([('cemento','Cemento'),('hierba','Hierba'),('moqueta','Moqueta'),('tierra','Tierra')])
 luz = fields.Selection([('si','Si'),('no','No')])
 precio = fields.Integer(string="Precio/hora de la pista")
 estado = fields.Selection([('disponible','Disponible'),('mantenimiento','Mantenimiento')])
 deporte_asociado=fields.Many2one('cdpelotas3763_y.deportes',string= "Deporte")
 #Campo reservas
 reservas=fields.One2many('cdpelotas3763_y.reservas',
     'instalacion',
     string="Reservas de la Instalacion"
  )
class Reservas(models.Model):
 _name = 'cdpelotas3763_y.reservas'
 _sql_constraints = [
  ('num_reserva_id',
  'UNIQUE (fecha_reservas,instalacion)',
  'Ya existe una reserva en ese intervalo de tiempo')]
 socio=fields.Many2one('cdpelotas3763_y.socios',string="Socio") 
 instalacion=fields.Many2one('cdpelotas3763_y.instalaciones',string="instalaciones")
 fecha_reservas=fields.Date(string="Fecha de Reserva",required=True)
 @api.one
 @api.constrains('fecha_reservas')
#  def _check_name_size(self):
#       ultima_fecha=self.env['cdpelotas3763_y.reservas'].browse(1,9999)
#   print("<script>alert('Datos 11')</script>")
#   if len(self.ultima_fecha) > 5:
#       raise ValidationError('Must have 5 chars! ')
 