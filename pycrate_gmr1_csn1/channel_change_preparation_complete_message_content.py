# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_gmr1_csn1/channel_change_preparation_complete_message_content.py
# * Created : 2023-10-24
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: ETSI TS 101 376-04-13
# section: 9.2.35a CHANNEL CHANGE PREPARATION COMPLETE
# top-level object: CHANNEL CHANGE PREPARATION COMPLETE message content

# external references
from pycrate_gmr1_csn1.rlc_sequence_number_ie import rlc_sequence_number_ie
from pycrate_gmr1_csn1.rrc_transaction_identifier_ie import rrc_transaction_identifier_ie
from pycrate_gmr1_csn1.rb_with_pdcp_information_ie import rb_with_pdcp_information_ie
from pycrate_gmr1_csn1.rb_activation_time_info_ie import rb_activation_time_info_ie
from pycrate_gmr1_csn1.integrity_protection_activation_info_ie import integrity_protection_activation_info_ie
from pycrate_gmr1_csn1.rb_identity_ie import rb_identity_ie
from pycrate_gmr1_csn1.cn_domain_identity_ie import cn_domain_identity_ie
from pycrate_gmr1_csn1.activation_time_ie import activation_time_ie
from pycrate_gmr1_csn1.start_ie import start_ie
from pycrate_gmr1_csn1.integrity_check_info_ie import integrity_check_info_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

uplink_counter_synchronisation_info_struct = CSN1List(name='uplink_counter_synchronisation_info_struct', list=[
  CSN1Bit(name='start_list', bit=2),
  CSN1List(num=([0], lambda x: x + 1), list=[
    CSN1Ref(name='cn_domain_identity', obj=cn_domain_identity_ie),
    CSN1Ref(name='start', obj=start_ie)]),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='rb_with_pdcp_information_list', bit=5),
    CSN1Ref(name='rb_with_pdcp_information', obj=rb_with_pdcp_information_ie, num=([1], lambda x: x + 1))])})])

channel_change_preparation_complete_message_content = CSN1List(name='channel_change_preparation_complete_message_content', list=[
  CSN1Ref(name='rrc_transaction_identifier', obj=rrc_transaction_identifier_ie),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='integrity_check_info', obj=integrity_check_info_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='uplink_integrity_protection_activation_info', obj=integrity_protection_activation_info_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='count_c_activation_time', obj=activation_time_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='radio_bearer_uplink_ciphering_activation_time_info', obj=rb_activation_time_info_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='uplink_counter_synchronisation_info', obj=uplink_counter_synchronisation_info_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='change_preparation_complete_rb_list', bit=5),
    CSN1List(num=([1], lambda x: x + 1), list=[
      CSN1Ref(name='rb_identity', obj=rb_identity_ie),
      CSN1Ref(name='last_received_rlc_block', obj=rlc_sequence_number_ie)])])})])

