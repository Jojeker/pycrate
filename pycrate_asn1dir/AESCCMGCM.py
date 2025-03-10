# -*- coding: UTF-8 -*-
# Code automatically generated by pycrate_asn1c

from pycrate_asn1rt.utils            import *
from pycrate_asn1rt.err              import *
from pycrate_asn1rt.glob             import make_GLOBAL, GLOBAL
from pycrate_asn1rt.dictobj          import ASN1Dict
from pycrate_asn1rt.refobj           import *
from pycrate_asn1rt.setobj           import *
from pycrate_asn1rt.asnobj_basic     import *
from pycrate_asn1rt.asnobj_str       import *
from pycrate_asn1rt.asnobj_construct import *
from pycrate_asn1rt.asnobj_class     import *
from pycrate_asn1rt.asnobj_ext       import *
from pycrate_asn1rt.init             import init_modules

class CMS_AES_CCM_and_AES_GCM:

    _name_  = 'CMS-AES-CCM-and-AES-GCM'
    _oid_   = [1, 2, 840, 113549, 1, 9, 16, 0, 32]
    
    _obj_ = [
        'aes',
        'id-aes128-CCM',
        'id-aes192-CCM',
        'id-aes256-CCM',
        'id-aes128-GCM',
        'id-aes192-GCM',
        'id-aes256-GCM',
        'CCMParameters',
        'AES-CCM-ICVlen',
        'GCMParameters',
        'AES-GCM-ICVlen',
        ]
    _type_ = [
        'CCMParameters',
        'AES-CCM-ICVlen',
        'GCMParameters',
        'AES-GCM-ICVlen',
        ]
    _set_ = [
        ]
    _val_ = [
        'aes',
        'id-aes128-CCM',
        'id-aes192-CCM',
        'id-aes256-CCM',
        'id-aes128-GCM',
        'id-aes192-GCM',
        'id-aes256-GCM',
        ]
    _class_ = [
        ]
    _param_ = [
        ]
    
    #-----< aes >-----#
    aes = OID(name='aes', mode=MODE_VALUE)
    aes._val = (2, 16, 840, 1, 101, 3, 4, 1)
    
    #-----< id-aes128-CCM >-----#
    id_aes128_CCM = OID(name='id-aes128-CCM', mode=MODE_VALUE)
    id_aes128_CCM._val = (2, 16, 840, 1, 101, 3, 4, 1, 7)
    
    #-----< id-aes192-CCM >-----#
    id_aes192_CCM = OID(name='id-aes192-CCM', mode=MODE_VALUE)
    id_aes192_CCM._val = (2, 16, 840, 1, 101, 3, 4, 1, 27)
    
    #-----< id-aes256-CCM >-----#
    id_aes256_CCM = OID(name='id-aes256-CCM', mode=MODE_VALUE)
    id_aes256_CCM._val = (2, 16, 840, 1, 101, 3, 4, 1, 47)
    
    #-----< id-aes128-GCM >-----#
    id_aes128_GCM = OID(name='id-aes128-GCM', mode=MODE_VALUE)
    id_aes128_GCM._val = (2, 16, 840, 1, 101, 3, 4, 1, 6)
    
    #-----< id-aes192-GCM >-----#
    id_aes192_GCM = OID(name='id-aes192-GCM', mode=MODE_VALUE)
    id_aes192_GCM._val = (2, 16, 840, 1, 101, 3, 4, 1, 26)
    
    #-----< id-aes256-GCM >-----#
    id_aes256_GCM = OID(name='id-aes256-GCM', mode=MODE_VALUE)
    id_aes256_GCM._val = (2, 16, 840, 1, 101, 3, 4, 1, 46)
    
    #-----< CCMParameters >-----#
    CCMParameters = SEQ(name='CCMParameters', mode=MODE_TYPE)
    _CCMParameters_aes_nonce = OCT_STR(name='aes-nonce', mode=MODE_TYPE)
    _CCMParameters_aes_nonce._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=7, ub=13)], ev=None, er=[])
    _CCMParameters_aes_ICVlen = INT(name='aes-ICVlen', mode=MODE_TYPE, typeref=ASN1RefType(('CMS-AES-CCM-and-AES-GCM', 'AES-CCM-ICVlen')), default=12)
    CCMParameters._cont = ASN1Dict([
        ('aes-nonce', _CCMParameters_aes_nonce),
        ('aes-ICVlen', _CCMParameters_aes_ICVlen),
        ])
    CCMParameters._ext = None
    
    #-----< AES-CCM-ICVlen >-----#
    AES_CCM_ICVlen = INT(name='AES-CCM-ICVlen', mode=MODE_TYPE)
    AES_CCM_ICVlen._const_val = ASN1Set(rv=[4, 6, 8, 10, 12, 14, 16], rr=[], ev=None, er=[])
    
    #-----< GCMParameters >-----#
    GCMParameters = SEQ(name='GCMParameters', mode=MODE_TYPE)
    _GCMParameters_aes_nonce = OCT_STR(name='aes-nonce', mode=MODE_TYPE)
    _GCMParameters_aes_ICVlen = INT(name='aes-ICVlen', mode=MODE_TYPE, typeref=ASN1RefType(('CMS-AES-CCM-and-AES-GCM', 'AES-GCM-ICVlen')), default=12)
    GCMParameters._cont = ASN1Dict([
        ('aes-nonce', _GCMParameters_aes_nonce),
        ('aes-ICVlen', _GCMParameters_aes_ICVlen),
        ])
    GCMParameters._ext = None
    
    #-----< AES-GCM-ICVlen >-----#
    AES_GCM_ICVlen = INT(name='AES-GCM-ICVlen', mode=MODE_TYPE)
    AES_GCM_ICVlen._const_val = ASN1Set(rv=[12, 13, 14, 15, 16], rr=[], ev=None, er=[])
    
    _all_ = [
        aes,
        id_aes128_CCM,
        id_aes192_CCM,
        id_aes256_CCM,
        id_aes128_GCM,
        id_aes192_GCM,
        id_aes256_GCM,
        _CCMParameters_aes_nonce,
        _CCMParameters_aes_ICVlen,
        CCMParameters,
        AES_CCM_ICVlen,
        _GCMParameters_aes_nonce,
        _GCMParameters_aes_ICVlen,
        GCMParameters,
        AES_GCM_ICVlen,
    ]

init_modules(CMS_AES_CCM_and_AES_GCM)
