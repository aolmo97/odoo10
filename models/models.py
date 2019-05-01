# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api
#Modelo Deporte
class Deporte(models.Model):
  _name = 'cdpelotas3763_y.deportes'

  nombre_deporte = fields.Char(string="Nombre del Deporte")
  instalaciones_asociadas=fields.One2many('cdpelotas3763_y.instalaciones',
     'deporte_asociado',
     string="Instalaciones Asociadas"
  )
#Modelo Socio
class Socio(models.Model):
 _name = 'cdpelotas3763_y.socios'

 num_socio = fields.Integer(string="Numero de socio")
 nombre = fields.Char(string="Nombre")
 apellidos = fields.Char(string="Apellidos")
 direccion = fields.Char(string="Direccion")
 telefono = fields.Integer(string="Teléfono")
 fecha_alta = fields.Date(string="Fecha de Alta")
 #Campo reservas
 #Modelo Instalaciones
class Instalaciones(models.Model):
 _name = 'cdpelotas3763_y.instalaciones'
 num_pista = fields.Integer(string="Numero de pista")
 nombre_pista = fields.Char(string="Nombre de Pista")
 superficie = fields.Selection([('cemento','Cemento'),('hierba','Hierba'),('moqueta','Moqueta'),('tierra','Tierra')])
 luz = fields.Selection([('si','Si'),('no','No')])
 precio = fields.Integer(string="Precio/hora de la pista")
 estado = fields.Selection([('disponible','Disponible'),('mantenimiento','Mantenimiento')])
 deporte_asociado=fields.Many2one('cdpelotas3763_y.deportes',string= "Deporte")
 #Campo reservas
class Reservas(models.Model):
 _name = 'cdpelotas3763_y.reservas'
 socio=fields.Many2one('cdpelotas3763_y.socios',string="Socio") 
 instalacion=fields.Many2one('cdpelotas3763_y.instalaciones',string="instalaciones")
 fecha_reserva=fields.DateTime(string="Fecha de Reserva")