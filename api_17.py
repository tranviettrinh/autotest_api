# cd D:\AnThinhPhat\pyc17
import requests, json
import pytest
import cx_Oracle
# start_Time="2022-06-16 09:07:40"
# end_Time="2022-06-17 09:07:41"
# queue_Id="180320673318032067331803206733180320673318032067331803206733"
# visitor_Username="zalo_522869426492085915"
# acc_url = "http://103.82.27.58:8029/api/getInfoChatMonitor?start_time="+start_Time+"&end_time="+end_Time+"&queue_id="+queue_Id+"&visitor_username="+visitor_Username
# acc_info = json.loads(requests.get(acc_url).text)


class ConverstationAPI(object):
	"""docstring for ClassName"""
	def __init__(self, startTime: str,endTime: str,queue_id:str):
		super(ConverstationAPI, self).__init__()
		self.startTime = startTime
		self.endTime = endTime
		self.queue_id = queue_id
	def api_url_1(self):
		url= f'http://103.82.27.58:8029/api/getInfoChatMonitor?start_time={self.startTime}&end_time={self.endTime}&queue_id={self.queue_id}'
		return url
# class TestCase(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, err: str, mess: str, start_time: str, end_time: str, queue_id: str):
# 		super(TestCase, self).__init__()
# 		self.err = err
# 		self.mess = mess
# 		self.start_time = start_time
# 		self.end_time = end_time
# 		self.queue_id = queue_id
class ConverstationAPIvisitor_username(object):
	"""docstring for ClassName"""
	def __init__(self, startTime: str,endTime: str,queue_id:str,thrid: str):
		super(ConverstationAPIvisitor_username, self).__init__()
		self.startTime = startTime
		self.endTime = endTime
		self.queue_id = queue_id
		self.thrid = thrid
	def api_url_2(self):
		url= f'http://103.82.27.58:8029/api/getInfoChatMonitor?start_time={self.startTime}&end_time={self.endTime}&queue_id={self.queue_id}&visitor_username={self.thrid}'
		return url
class ConverstationAPIagent_name(ConverstationAPIvisitor_username):
	"""docstring for ClassName"""
	def api_url_3(self):
		url= f'http://103.82.27.58:8029/api/getInfoChatMonitor?start_time={self.startTime}&end_time={self.endTime}&queue_id={self.queue_id}&agent_name={self.thrid}'
		return url
class ConverstationAPIsource(ConverstationAPIvisitor_username):
	"""docstring for ClassName"""
	def api_url_4(self):
		url= f'http://103.82.27.58:8029/api/getInfoChatMonitor?start_time={self.startTime}&end_time={self.endTime}&queue_id={self.queue_id}&source={self.thrid}'
		return url
class ConverstationAPIconversation_id(ConverstationAPIvisitor_username):
	"""docstring for ClassName"""
	def api_url_5(self):
		url= f'http://103.82.27.58:8029/api/getInfoChatMonitor?start_time={self.startTime}&end_time={self.endTime}&queue_id={self.queue_id}&conversation_id={self.thrid}'
		return url

		

class Conversation(object):
		"""docstring for ClassName"""
		def __init__(self, conversationId,startTime,endTime,creatorAgentId,visitorUsername,queueFirstTime,firstRingTime,firstAnswerTime,endReason,agentName,queueId,countAnswer,countAnswerAll,processDuration,listMessage):
			super(Conversation, self).__init__()
			self.conversationId = conversationId # 0
			self.startTime = startTime
			self.endTime = endTime #1
			self.creatorAgentId = creatorAgentId #2
			self.visitorUsername = visitorUsername #3
			self.queueFirstTime = queueFirstTime #4
			self.firstRingTime = firstRingTime # 0
			self.firstAnswerTime = firstAnswerTime # 0
			self.endReason = endReason #1
			self.agentName = agentName #2
			self.queueId = queueId #3
			self.countAnswer = countAnswer #4
			self.countAnswerAll = countAnswerAll # 0
			self.processDuration = processDuration #1
			self.listMessage =listMessage  #1

@pytest.fixture
def list_test_case():
	data=[["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673"],# test_start_time_1
			# start_time
			["1","Start time sai định dạng","2022-06-16 09:07:400","2022-06-17 09:07:41","180320673"],# test_start_time_2
			["1","Start time sai định dạng","2022-06-16 09:07:40tr","2022-06-17 09:07:41","180320673"],# test_start_time_3
			["1","Start time sai định dạng","         ","2022-06-17 09:07:41","180320673"],# test_start_time_4
			["1","Thiếu tham số start_time","","2022-06-17 09:07:41","180320673"],# test_start_time_5
			["1","Từ Start time đến End Time không được quá 31 ngày","2022-02-28 09:07:40","2022-03-30 09:07:41","180320673"],# test_start_time_6
			["1","Từ Start time đến End Time không được quá 31 ngày","2022-02-28 09:07:40","2022-03-30 09:07:41","180320673"],# test_start_time_7
			["1","Từ Start time đến End Time không được quá 31 ngày","2022-02-29 09:07:40","2022-03-31 09:07:41","180320673"],# test_start_time_8
			["1","Start time không thể lớn hơn hoặc bằng End time","2022-07-17 09:07:41","2022-06-17 09:07:41","180320673"],# test_start_time_9
			["1","Start time không thể lớn hơn hoặc bằng End time","2022-06-17 09:07:41","2022-06-17 09:07:41","180320673"],# test_start_time_10
			# end_time
			["1","End time sai định dạng","2022-06-16 09:07:40","2022-06-17 09:07:410","180320673"],# test_end_time_11
			["1","End time sai định dạng","2022-06-16 09:07:40","2022-06-17 09:07:41tr","180320673"],# test_end_time_12
			["1","End time sai định dạng","2022-06-17 09:07:41","           ","180320673"],# test_end_time_13
			["1","Thiếu tham số end_time","2022-06-17 09:07:41","","180320673"],# test_end_time_14
			["1","Từ Start time đến End Time không được quá 31 ngày","2022-01-28 09:07:40","2022-02-27 09:07:41","180320673"],# test_end_time_15
			# queue_id
			["1","Thiếu tham số queue_id","2022-06-16 09:07:40","2022-06-17 09:07:41",""], # test_queue_id_16
			["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","                 "], # test_queue_id_17
			["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","18032067318035180320673180354"], # test_queue_id_18
			["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673180351803206731803544"], # test_queue_id_19
			["1","Queue id vượt quá số ký tự cho phép","2022-06-16 09:07:40","2022-06-17 09:07:41","1803206731803518032067318035444"], # test_queue_id_20
			# visitor_username
			["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","zalo_2509979009293428495"], # test_visitor_username_21
			["1","Định danh khách hàng không tồn tại","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673",""], # test_visitor_username_22
			["1","Định danh khách hàng không tồn tại","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","              "], # test_visitor_username_23
			["1","Định danh khách hàng không tồn tại","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111499"], # test_visitor_username_24
			["1","Định danh khách hàng không tồn tại","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111500"], # test_visitor_username_25
			["1","Định danh khách hàng vượt quá số ký tự cho phép","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111500"], # test_visitor_username_26
			#agent_name
			["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","fo10"], # test_agent_name_27
			["1","Định danh tư vấn viên không tồn tại","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673",""], # test_agent_name_28
			["1","Định danh tư vấn viên không tồn tại","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","          "], # test_agent_name_29
			["1","Định danh tư vấn viên không tồn tại","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111499"], # test_agent_name_30
			["1","Định danh tư vấn viên không tồn tại","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111500"], # test_agent_name_31
			["1","Định danh tư vấn viên vượt quá số ký tự cho phép","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111500"], # test_agent_name_32
			#source
			["1","Kênh tiếp nhận sai định dạng","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673",""], # test_source_33
			["1","Kênh tiếp nhận sai định dạng","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","            "],# test_source_34
			["1","Kênh tiếp nhận sai định dạng","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","abc"],# test_source_35
			["1","Kênh tiếp nhận sai định dạng","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","3.2"],# test_source_36
			["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","1"],# test_source_37
			["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","2"],# test_source_38
			["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","3"],# test_source_39
			["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","4"],# test_source_40
			["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","5"],# test_source_41
			["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","6"],# test_source_42
			["1","Kênh tiếp nhận không tồn tại trên hệ thống","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","7"],# test_source_43
			# conversation_id
			["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","10311454"],# test_conversation_id_44
			["1","Định danh cuộc hội thoại không tồn tại","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673",""],# test_conversation_id_45
			["1","Định danh cuộc hội thoại không tồn tại","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","               "],# test_conversation_id_46
			["1","Định danh cuộc hội thoại không tồn tại","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","11111111111114"],# test_conversation_id_47
			["1","Định danh cuộc hội thoại không tồn tại","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","111111111111115"],# test_conversation_id_48
			["1","Định danh cuộc hội thoại vượt quá số ký tự cho phép","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673","1111111111111116"],# test_conversation_id_49

			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			[],
			
			]
	return data
# @pytest.fixture
# def list_test_case():
# 	data=[["0","Thành công","2022-02-29 09:07:40","2022-03-31 09:07:40","180320673"]]
# 	return data

# @pytest.fixture
# def test_case():
# 	data=["0","Thành công","2022-06-16 09:07:40","2022-06-17 09:07:41","180320673"]
# 	return data


def test_start_time_1(list_test_case): 
	data=list_test_case[0]
	converstation=ConverstationAPI(data[2],data[3],data[4])
	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
	mess =str(acc_info['message'])
	err = str(acc_info['errorCode'])
	dataApi =(acc_info['data'])
	dulieu=[]
	dulieudb=[]
	for i in acc_info['data']:
		conversationId=str(i['conversationId'])
		startTime=str(i['startTime'])
		endTime=str(i['endTime'])
		creatorAgentId=str(i['creatorAgentId'])
		visitorUsername=str(i['visitorUsername'])
		queueFirstTime=str(i['queueFirstTime'])
		firstRingTime=str(i['firstRingTime'])
		firstAnswerTime=str(i['firstAnswerTime'])
		endReason=str(i['endReason'])
		agentName=str(i['agentName'])
		queueId=str(i['queueId'])
		countAnswer=str(i['countAnswer'])
		countAnswerAll=str(i['countAnswerAll'])
		processDuration=str(i['processDuration'])
		listMessage= str(i['listMessage'])

		conver=Conversation(conversationId,startTime,endTime,creatorAgentId,visitorUsername,queueFirstTime,firstRingTime,firstAnswerTime,endReason,agentName,queueId,countAnswer,countAnswerAll,processDuration,listMessage)
		dulieu=[str(conver.conversationId),str(conver.startTime),str(conver.endTime),str(conver.creatorAgentId),str(conver.visitorUsername),str(conver.queueFirstTime),str(conver.firstRingTime),str(conver.firstAnswerTime),str(conver.endReason),str(conver.agentName),str(conver.queueId),str(conver.countAnswer),str(conver.countAnswerAll),str(conver.processDuration)]
		dulieu.append(dulieu)

	try:
		con = cx_Oracle.connect('ipcc_chat/Hoangbao09@103.82.22.149:9521/ECONTACT')

		# Now execute the sqlquery
		cursor = con.cursor()

		# Creating a table employee
		def output_type_handler(cursor, name, default_type, size, precision, scale):
			if default_type == cx_Oracle.DB_TYPE_CLOB:
				return cursor.var(cx_Oracle.DB_TYPE_LONG, arraysize=cursor.arraysize)
			if default_type == cx_Oracle.DB_TYPE_BLOB:
				return cursor.var(cx_Oracle.DB_TYPE_LONG_RAW, arraysize=cursor.arraysize)
		con.outputtypehandler = output_type_handler
		query = "select * FROM CONVERSATION where (end_time >= TO_DATE('2022-06-16 09:07:40', 'YYYY-MM-DD hh24:mi:ss') and end_time <= TO_DATE('2022-06-17 09:07:41', 'YYYY-MM-DD hh24:mi:ss')) and queue_id =  180320673"
		cursor.execute(query)
		rows = cursor.fetchall()
		for i in range(0,len(rows)):
			dulieudb.append(str(rows[i][0]))

	except cx_Oracle.DatabaseError as e:
		print("There is a problem with Oracle", e)

	# by writing finally if any error occurs
	# then also we can close the all database operation
	finally:
		if cursor:
			cursor.close()
		if con:
			con.close()
		
	status = str(data[0])
	note= str(data[1])
	assert mess == note 
	assert err == status
	assert dataApi != None
	assert dulieu==dulieudb
# def test_start_time_2(list_test_case): 
# 	data=list_test_case[1]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_start_time_3(list_test_case): 
# 	data=list_test_case[2]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == 'None'
# def test_start_time_4(list_test_case): 
# 	data=list_test_case[3]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_start_time_5(list_test_case): 
# 	data=list_test_case[4]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_start_time_6(list_test_case): 
# 	data=list_test_case[5]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_start_time_7(list_test_case): 
# 	data=list_test_case[6]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_start_time_8(list_test_case): 
# 	data=list_test_case[7]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_start_time_9(list_test_case): 
# 	data=list_test_case[8]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_start_time_10(list_test_case): 
# 	data=list_test_case[9]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# ##############################################################################	END_TIME
# def test_end_time_11(list_test_case): 
# 	data=list_test_case[10]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_end_time_12(list_test_case): 
# 	data=list_test_case[11]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_end_time_13(list_test_case): 
# 	data=list_test_case[12]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_end_time_14(list_test_case): 
# 	data=list_test_case[13]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_end_time_15(list_test_case): 
# 	data=list_test_case[14]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# ############################################################################## QUEUE_ID
# def test_queue_id_16(list_test_case): 
# 	data=list_test_case[15]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_queue_id_17(list_test_case): 
# 	data=list_test_case[16]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == []
# def test_queue_id_18(list_test_case): 
# 	data=list_test_case[17]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_queue_id_19(list_test_case):
# 	data=list_test_case[18]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status

# def test_queue_id_20(list_test_case): 
# 	data=list_test_case[19]
# 	converstation=ConverstationAPI(data[2],data[3],data[4])
# 	acc_info = json.loads(requests.get(converstation.api_url_1()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =str(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# ################################################################################# visitor_username
# def test_visitor_username_21(list_test_case): 
# 	data=list_test_case[20]
# 	converstation=ConverstationAPIvisitor_username(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_2()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi != None
# def test_visitor_username_22(list_test_case): 
# 	data=list_test_case[21]
# 	converstation=ConverstationAPIvisitor_username(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_2()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_visitor_username_23(list_test_case): 
# 	data=list_test_case[22]
# 	converstation=ConverstationAPIvisitor_username(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_2()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_visitor_username_24(list_test_case): 
# 	data=list_test_case[23]
# 	converstation=ConverstationAPIvisitor_username(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_2()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_visitor_username_25(list_test_case): 
# 	data=list_test_case[24]
# 	converstation=ConverstationAPIvisitor_username(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_2()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_visitor_username_26(list_test_case): 
# 	data=list_test_case[25]
# 	converstation=ConverstationAPIvisitor_username(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_2()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# ################################################################################# agent_name
# def test_agent_name_27(list_test_case): 
# 	data=list_test_case[26]
# 	converstation=ConverstationAPIagent_name(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_3()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi != None
# def test_agent_name_28(list_test_case): 
# 	data=list_test_case[27]
# 	converstation=ConverstationAPIagent_name(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_3()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_agent_name_29(list_test_case): 
# 	data=list_test_case[28]
# 	converstation=ConverstationAPIagent_name(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_3()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_agent_name_30(list_test_case): 
# 	data=list_test_case[29]
# 	converstation=ConverstationAPIagent_name(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_3()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_agent_name_31(list_test_case): 
# 	data=list_test_case[30]
# 	converstation=ConverstationAPIagent_name(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_3()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_agent_name_32(list_test_case): 
# 	data=list_test_case[31]
# 	converstation=ConverstationAPIagent_name(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_3()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# ################################################################################# source
# def test_source_33(list_test_case): 
# 	data=list_test_case[32]
# 	converstation=ConverstationAPIsource(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_4()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_source_34(list_test_case): 
# 	data=list_test_case[33]
# 	converstation=ConverstationAPIsource(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_4()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_source_35(list_test_case): 
# 	data=list_test_case[34]
# 	converstation=ConverstationAPIsource(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_4()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_source_36(list_test_case): 
# 	data=list_test_case[35]
# 	converstation=ConverstationAPIsource(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_4()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_source_37(list_test_case): 
# 	data=list_test_case[36]
# 	converstation=ConverstationAPIsource(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_4()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi != None
# def test_source_38(list_test_case): 
# 	data=list_test_case[37]
# 	converstation=ConverstationAPIsource(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_4()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi != None
# def test_source_39(list_test_case): 
# 	data=list_test_case[38]
# 	converstation=ConverstationAPIsource(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_4()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi != None
# def test_source_40(list_test_case): 
# 	data=list_test_case[39]
# 	converstation=ConverstationAPIsource(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_4()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi != None
# def test_source_41(list_test_case): 
# 	data=list_test_case[40]
# 	converstation=ConverstationAPIsource(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_4()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi != None
# def test_source_42(list_test_case): 
# 	data=list_test_case[41]
# 	converstation=ConverstationAPIsource(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_4()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi != None
# def test_source_43(list_test_case): 
# 	data=list_test_case[42]
# 	converstation=ConverstationAPIsource(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_4()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# ####################################################################################### conversation_id
# def test_conversation_id_44(list_test_case): 
# 	data=list_test_case[43]
# 	converstation=ConverstationAPIconversation_id(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_5()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi != None
# def test_conversation_id_45(list_test_case): 
# 	data=list_test_case[44]
# 	converstation=ConverstationAPIconversation_id(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_5()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_conversation_id_46(list_test_case): 
# 	data=list_test_case[45]
# 	converstation=ConverstationAPIconversation_id(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_5()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_conversation_id_47(list_test_case): 
# 	data=list_test_case[46]
# 	converstation=ConverstationAPIconversation_id(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_5()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_conversation_id_48(list_test_case): 
# 	data=list_test_case[47]
# 	converstation=ConverstationAPIconversation_id(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_5()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None
# def test_conversation_id_49(list_test_case): 
# 	data=list_test_case[48]
# 	converstation=ConverstationAPIconversation_id(data[2],data[3],data[4],data[5])
# 	acc_info = json.loads(requests.get(converstation.api_url_5()).text)
# 	mess =str(acc_info['message'])
# 	err = str(acc_info['errorCode'])
# 	dataApi =(acc_info['data'])
# 	status = str(data[0])
# 	note= str(data[1])
# 	assert mess == note 
# 	assert err == status
# 	assert dataApi == None

