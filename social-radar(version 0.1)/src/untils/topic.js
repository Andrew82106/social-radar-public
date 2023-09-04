// 首页柱状图数据结构
// source:网站名称
// id:网站id
// topictList {  //不同事件的访问量的数据合集
	// "topict": "事件名称",
	// "total": "访问量"
// }

const topic={
	"message": "请求成功",
	"code": 200,
	"success": true,
	"data": {
		"totalRows": 4,
		"resultList": [{
			"source": "facebook",
			"id": "1",
			"topictList": [{
				"topict": "810大埔遊行",
				"total": "1542"
			}, {
				"topict": "航空界机场集会test",
				"total": "321"
			}, {
				"topict": "8.5全港大罢工",
				"total": "255"
			}, {
				"topict": "反送中大游行",
				"total": "544"
			}, {
				"topict": "反蒙面恶法",
				"total": "155"
			}]
		},{
			"source": "Twitter",
			"id": "3",
			"topictList": [{
				"topict": "810大埔遊行",
				"total": "282"
			}, {
				"topict": "航空界机场集会",
				"total": "901"
			}, {
				"topict": "8.5全港大罢工",
				"total": "125"
			}, {
				"topict": "反送中大游行",
				"total": "375"
			}, {
				"topict": "反蒙面恶法",
				"total": "155"
			}]
		}, {
			"source": "Instagram",
			"id": "4",
			"topictList": [{
				"topict": "810大埔遊行",
				"total": "819"
			}, {
				"topict": "航空界机场集会",
				"total": "797"
			}, {
				"topict": "8.5全港大罢工",
				"total": "888"
			}, {
				"topict": "反送中大游行",
				"total": "267"
			}, {
				"topict": "反蒙面恶法",
				"total": "55"
			}]
		}, {
			"source": "Youtube",
			"id": "5",
			"topictList": [{
				"topict": "810大埔遊行",
				"total": "655"
			}, {
				"topict": "航空界机场集会",
				"total": "730"
			}, {
				"topict": "8.5全港大罢工",
				"total": "155"
			}, {
				"topict": "反送中大游行",
				"total": "893"
			}, {
				"topict": "反蒙面恶法",
				"total": "413"
			}]
		}, {
			"source": "网站",
			"id": "6",
			"topictList": [{
				"topict": "810大埔遊行",
				"total": "323"
			}, {
				"topict": "航空界机场集会",
				"total": "325"
			}, {
				"topict": "8.5全港大罢工",
				"total": "926"
			}, {
				"topict": "反送中大游行",
				"total": "253"
			}, {
				"topict": "反蒙面恶法",
				"total": "505"
			}]
		}]
	}
}
export default topic