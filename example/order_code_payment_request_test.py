#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import time
import io

from com.alipay.ams.api.model.order import Order
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.merchant import Merchant
from com.alipay.ams.api.model.store import Store
from com.alipay.ams.api.request.pay.order_code_payment_request import OrderCodePaymentRequest
from com.alipay.ams.api.response.pay.alipay_pay_response import AlipayPayResponse
from com.alipay.ams.api.default_alipay_client import DefaultAlipayClient

class OrderCodePaymentRequestTest(unittest.TestCase):
	def test_order_code(self):

		TEST_CLIENT_ID = 'T_385XSM502Y108602A'
		script_dir = os.path.dirname(__file__)
		with io.open(os.path.join(script_dir, '../private-pkcs1.pem'), encoding = 'utf-8') as pri, io.open(os.path.join(script_dir, '../public.pem'), encoding = 'utf-8') as pub:
			PRIVATE_KEY = pri.read()
			alipay_public_key = pub.read()




		order = Order()
		order.order_description = 'This is an order.'
		order.order_amount = Amount('USD', 1231)

		merchant = Merchant()
		merchant.reference_merchant_id = 'seller2322174590000'
		merchant.merchant_mcc = '7011'
		merchant.merchant_name = 'Some_Mer'

		store = Store()
		store.store_mcc = '7011'
		store.store_name = 'Some_Store'
		store.reference_store_id = 'store232217459000011'

		merchant.store = store
		order.merchant = merchant

		orderCodeReq = OrderCodePaymentRequest(payment_request_id=int(time.time()), order=order, currency="USD", amount_in_cents=1231, payment_notify_url='http://alipay.com/test')

		body = orderCodeReq.to_ams_json()
		#print(body)
		#print('-' * 120)
		#
		#DATA = body.encode('utf-8')
		#requestTime = get_cur_iso8601_time()
		#
		#req = urllib.request.Request(url='https://open-na.alipay.com/ams/api/v1/payments/pay', data=DATA,method='POST')
		#req.add_header("content-type","application/json; charset=UTF-8")
		#req.add_header("client-id",TEST_CLIENT_ID)
		#req.add_header("request-time",requestTime)
		#req.add_header("signature","algorithm=RSA256,keyVersion=1,signature=" + sign(orderCodeReq.http_method.value, orderCodeReq.path, TEST_CLIENT_ID, requestTime, body, PRIVATE_KEY))
		#
		#with urllib.request.urlopen(req) as f:
		#	#print(f.status)
		#	print(f.read().decode('utf-8'))
		#	print(f.headers)

		default_alipay_client = DefaultAlipayClient("https://open-na.alipay.com", TEST_CLIENT_ID, PRIVATE_KEY, alipay_public_key)

		rsp_body = default_alipay_client.execute(orderCodeReq)

		response = AlipayPayResponse(rsp_body)

		#print(rsp_body)
		#print('-' * 120)

		def onF(response):
			print('onF: ' + response.result.result_code)

		def onU(response):
			print('onU: ' + response.result.result_code)

		def onS(response):
			print("%s, %s" % (response.payment_id, response.order_code_form.code_details[0].code_value))
			self.assertIsNotNone(response.order_code_form.code_details[0].code_value)

		{
			'F': onF,
			'U': onU,
			'S': onS
		}.get(response.result.result_status.value)(response)

