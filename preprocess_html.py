from ast import parse
import re
CLEANR = re.compile('<.*?>') 

text_string = """
<table class="table_basic table_faq_cs">
			   <colgroup>
				   <col width="8%">
				   <col width="">
			   </colgroup>
			   <thead>
				   <tr>
					   <th scope="col">번호</th>
					   <th scope="col">내용</th>
				   </tr>
			   </thead>
			   <tbody>
										<tr>
					   <td style="border: none">1</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_140', '', ''); return false;">관심 있는 브랜드의 소식을 받아보고 싶어요</a></td>
					</tr>
					<tr id="faq_140" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							<p>브랜드 페이지에서 ♡모양의 '좋아요'를 누르면 관심 브랜드로 추가됩니다.<br><br>
* 관심 브랜드의 신제품 발매, 세일 소식 등을 앱으로 알림 수신 가능<br><br>
<br><br>
■ 관심 브랜드 관리 방법<br><br>
- PC:&nbsp;<a href="https://store.musinsa.com/app/mypage/favorite_goods" rel="nofollow" target="_blank"><span style="color:#3498db;">'마이페이지 &gt; 나의 쇼핑 활동 &gt; 좋아요'</span></a>에서 확인<br><br>
- 모바일: 앱 하단 메뉴<span style="color:#3498db;">&nbsp;</span><a href="https://m.store.musinsa.com/app/mypage/wishlist" rel="nofollow" target="_blank"><span style="color:#3498db;">'♡ 좋아요'</span></a>에서 확인</p>							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=140</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">2</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_142', '', ''); return false;">사이즈 문의를 하고 싶은데, 간편하게 확인 가능한 기능이 있나요?</a></td>
					</tr>
					<tr id="faq_142" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							<p>'마이사이즈'에서 신체 정보와 실측을 입력하면 회원님에게 맞는 사이즈를 자동으로 추천합니다.<br><br>
* 실측은 '직접 입력' 또는 '최근 구매 내역'을 통해 기재 가능<br><br>
<br><br>
■ 실측 사이즈 입력 방법<br><br>
- PC:&nbsp;<a href="https://store.musinsa.com/app/mypage/mysize_new" rel="nofollow" target="_blank"><span style="color:#3498db;">'마이페이지 &gt; 나의 쇼핑 활동 &gt; 마이 사이즈'</span></a>에서 입력<br><br>
- 모바일:&nbsp;<a href="https://m.store.musinsa.com/app/mypage/mysize_new" rel="nofollow" target="_blank"><span style="color:#3498db;">'마이페이지 &gt; 쇼핑정보 &gt; 마이사이즈 관리'</span></a>에서 입력<br><br>
<br><br>
※ 입력된 실측을 기준으로 상품의 상세페이지 내 '사이즈'에서 옵션별 사이즈와 비교하고 추천받을 수 있습니다.</p>							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=142</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">3</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_143', '', ''); return false;">다른 구매자의 사이즈와 비교해서 구매에 참고 하고 싶어요.</a></td>
					</tr>
					<tr id="faq_143" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							<p>제품 상세 페이지 사이즈 추천에서 사이즈 별로 구매한 다른 고객들의 신체 정보와 사이즈 만족도를 확인할 수 있습니다.&nbsp;</p>							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=143</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">4</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_144', '', ''); return false;">상품 검색을 하는 방법은 어떤 것들이 있나요?</a></td>
					</tr>
					<tr id="faq_144" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							<p>무신사 스토어에서 상품 구분을 하는 방법은 매우 다양합니다. 브랜드, 카테고리뿐만 아니라, 스타일, 컬러로도 구분이 가능합니다. 또한 검색 창을 통하여 상품의 세부 품목 검색을 할 수도 있습니다.<br><br>
좌측의 메뉴에서는 카테고리별, 스타일별, 브랜드별, 숍인숍 별로 브랜드를 구분할 수 있으며, 브랜드 페이지에서는 성별 / 제품 카테고리별 / 컬러별 / 가격대별로 제품을 구분하여 찾을 수 있습니다.</p>							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=144</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">5</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_148', '', ''); return false;">품절 시 처리 방법에 대해 알고 싶어요.</a></td>
					</tr>
					<tr id="faq_148" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							<p>주문 후 품절 발생 시 결제하신 수단으로 별도의 안내 없이 환불해 드립니다.</p>							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=148</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">6</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_149', '', ''); return false;">무신사 만의 다양한 할인 혜택을 자세히 알고 싶습니다.</a></td>
					</tr>
					<tr id="faq_149" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							<p>무신사 스토어에서는 적립금 선할인, 쿠폰 할인, 회원 할인 등의 다양한 혜택을 제공합니다.</p><br>
<br>
<p>[적립금 선할인]<br><br>
상품 구매 시 지급되는 적립금을 미리 사용하여 결제 시 할인받을 수 있습니다.</p><br>
<br>
<p>[쿠폰]<br><br>
회원 등급 별 월 정기 쿠폰, 생일 쿠폰, 명절 쿠폰, 오프라인 쿠폰 등 다양한 쿠폰이 지급됩니다.</p><br>
<br>
<p>[회원 할인]<br><br>
회원 등급에 따라 주문 시 할인받을 수 있으며, 등급 별 할인은 <strong><a href="https://store.musinsa.com/app/content/s/cs/benefit_01" target="_blank"><span style="color:#3498db;">[회원 혜택]</span></a></strong>에서 확인할 수 있습니다.&nbsp;</p>							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=149</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">7</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_154', '', ''); return false;">후기 작성 규정이 어떻게 되나요?</a></td>
					</tr>
					<tr id="faq_154" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							<p>후기는 일반 후기 / 상품 사진 후기 / 스타일 후기로 구성되어 있으며, 상품 별로 모든 후기 등록이 가능합니다. 규정에 맞지 않는 후기는 적립금이 지급되지 않으니 아래의 규정을 참고해 주시기 바랍니다.&nbsp;<br><br>
<br><br>
[일반 후기]<br><br>
- 20자 이상의 텍스트로만 작성하는 후기입니다. 단순 문자 및 기호의 나열/반복은 제한됩니다.<br><br>
- 적립금 지급 범위 : 500원<br><br>
<br><br>
[상품 사진 후기]<br><br>
- 포장이 제거된 상품의 형태가 프레임 내에 또렷하게 보이도록 직접 촬영한 사진을 등록해야 합니다.<br><br>
- 후기 내용은 20자 이상 작성합니다. 단순 문자 및 기호의 나열/반복은 적립금이 지급되지 않습니다.<br><br>
- 이미지 폭이 300px 미만이거나 2000px을 초과하면 등록되지 않습니다.<br><br>
- 적립금 범위 : 1000원<br><br>
<br><br>
[스타일 후기]<br><br>
- 상품의 식별이 가능하도록 착용한 상태에서 직접 촬영한 사진이어야 하며, 착용이 어려운 상품은 휴대합니다.<br><br>
- 사진 등록 시 얼굴은 제외 가능하지만 어깨부터 발끝까지 모두 사진 안에 보여야 합니다.<br><br>
- 후기 내용은 20자 이상 작성합니다. 단순 문자 및 기호의 나열/반복은 적립금이 지급되지 않습니다.<br><br>
- 이미지 폭이 300px 미만이거나 2000px을 초과하면 등록되지 않습니다.<br><br>
- 적립금 범위 : 2000원<br><br>
<br><br>
이메일, 휴대전화 번호 등의 개인 정보/광고/비속어가 포함된 후기는 블라인드 처리됩니다.<br><br>
등록한 후기는 공개되어 회원이 조회 가능하며, 댓글이 등록될 수 있습니다.<br><br>
작성된 후기는 무신사 홍보 콘텐츠로 사용될 수 있습니다.</p>							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=154</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">8</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_167', '', ''); return false;">후기 사진을 도용하면 어떤 불이익이 있나요?</a></td>
					</tr>
					<tr id="faq_167" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							<p>후기 사진 도용이 적발될 시에는 이미 작성된 후기 및 적발일로부터 3개월간 작성된 후기에 대하여 적립금 지급이 중단됩니다.&nbsp;<br><br>
또한 해당 후기 종류에 지급되는 최대 적립금의 2배가 환수되며, 무신사 커뮤니티 이용이 1년간 정지됩니다.</p>							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=167</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">9</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_217', '', ''); return false;">로그인 포인트가 지급되지 않았어요.</a></td>
					</tr>
					<tr id="faq_217" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							<p>로그인 포인트는 당일 최초 로그인 시 1회 지급됩니다.<br><br>
로그인 상태로 유지가 되어 있는 경우에는 지급되지 않으므로 재로그인 해야 합니다.</p>							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=217</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">10</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_229', '', ''); return false;">카드사 즉시 할인 프로모션 쿠폰은 어떻게 적용할 수 있나요?</a></td>
					</tr>
					<tr id="faq_229" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							<p>[PC]<br><br>
1. 주문 작성 단계 중 결제 수단 우측의 결제 프로모션 내용을 확인 후, 해당 카드사를 선택하여&nbsp;결제를 진행합니다.</p><br>
<br>
<p>2. 이용 약관 동의 후 다음 단계로 이동합니다.</p><br>
<br>
<p>3. 할인받기를 눌러 쿠폰을 다운로드합니다.</p><br>
<br>
<p>4. 쿠폰 할인이 적용되었습니다. 다음 단계를 눌러 최종 결제를 진행합니다.<br><br>
<br><br>
[MOBILE, APP]<br><br>
1. 카드사 즉시 할인 프로모션이 진행 중인 경우, 해당 카드사를 선택 후 결제하기를 진행합니다.</p><br>
<br>
<p>2. 이용 약관에 동의합니다. 동의 후 쿠폰 선택이 가능합니다.</p><br>
<br>
<p>3. 쿠폰을 선택하여 할인 적용을 받습니다. 다음을 눌러 최종 결제를 진행합니다.</p>							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=229</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">11</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_235', '', ''); return false;">관심(좋아요) 브랜드 알림이 오지 않아요.</a></td>
					</tr>
					<tr id="faq_235" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							아래의 2가지 방법으로 등록 및 알림 설정을 확인해주세요.<br><br>
* 모두 확인해도 해결되지 않을 경우 고객센터(1544-7199 또는 1:1문의)로 문의<br><br>
<br><br>
1. 관심 브랜드 등록 확인하기<br><br>
- PC:&nbsp;<a href="https://store.musinsa.com/app/mypage/favorite_goods" rel="nofollow" target="_blank"><span style="color:#3498db;">'마이페이지 &gt; 나의 쇼핑 활동 &gt; 좋아요'</span></a>에서 확인<br><br>
- 모바일: 앱 하단 메뉴&nbsp;<a href="https://m.store.musinsa.com/app/mypage/wishlist" rel="nofollow" target="_blank"><span style="color:#3498db;">'♡ 좋아요'</span></a>에서 확인<br><br>
<br><br>
2. 앱 알림 설정 확인하기<br><br>
- 보유하신 휴대전화의 설정에서 무신사 앱에 대한 알림 버튼을 확인(설정 &gt; 알림)<br><br>
<br><br>
※ 관심 브랜드 소식은 무신사 앱으로만 알림이 전송됩니다.							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=235</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">12</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_255', '', ''); return false;">후기는 언제까지 작성할 수 있나요?</a></td>
					</tr>
					<tr id="faq_255" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							주문 상태가&nbsp;구매확정일 때부터 작성이 가능하며,&nbsp;구매확정일&nbsp;기준&nbsp;90일을 초과하면 작성이 불가능합니다.&nbsp;<br><br>
마이 페이지 &gt; 나의 쇼핑 활동 &gt;&nbsp;<strong><a href="https://store.musinsa.com/app/mypage/write_review" target="_blank"><span style="color:#3498db;">[구매 후기]</span></a></strong>에서 작성할 수 있습니다.							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=255</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">13</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_256', '', ''); return false;">작성한 후기는 삭제할 수 있나요?</a></td>
					</tr>
					<tr id="faq_256" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							작성한 후기에 댓글 또는 적립금이 지급되지 않은 경우 삭제 가능합니다.&nbsp;<br><br>
마이 페이지 → 나의 쇼핑 활동 → 구매 후기 → <strong><a href="https://store.musinsa.com/app/mypage/review" target="_blank"><span style="color:#3498db;">[후기 내역]</span></a></strong>에서 삭제할 수 있습니다. 단, 삭제한 후기는 복구할 수 없으며 다시 작성이 불가능합니다.							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=256</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">14</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_257', '', ''); return false;">작성한 후기는 어디에 노출되나요?</a></td>
					</tr>
					<tr id="faq_257" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							작성된 후기는 적립금 지급 여부 상관없이 무신사 스토어 메인 페이지, 콘텐츠 &gt; 회원 후기, 브랜드 및 상품 페이지에 노출됩니다.							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=257</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">15</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_258', '', ''); return false;">후기 댓글에 욕설이 있어요. 어떻게 해야 하나요?</a></td>
					</tr>
					<tr id="faq_258" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							신고 접수를 해주시면 댓글 처리와 함께 작성 회원에 대해 게시글 및 댓글 작성을 제한합니다.&nbsp;<br><br>
해당 댓글에 있는 신고 버튼을 눌러 접수해 주시기 바랍니다.							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=258</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">16</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_292', '', ''); return false;">[이용팁] 알림 설정(앱푸시)은 어떻게 변경하나요?</a></td>
					</tr>
					<tr id="faq_292" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							모바일 앱에서 아래 2가지 경로를 통해 알림 설정이 가능합니다.<br><br>
<br><br>
1. 앱 &gt; 알림<br><br>
모바일 앱 화면 왼쪽 위의 종 모양을 클릭한 후 오른쪽 위의<a href="https://www.musinsa.com/member/mypage/myinfo/notice" rel="nofollow" target="_blank">&nbsp;<span style="color:#3498db;">'설정'</span></a>에서 변경<br><br>
<br><br>
2. 앱 &gt; 마이페이지<br><br>
<a href="https://www.musinsa.com/member/mypage/myinfo/notice" rel="nofollow" target="_blank"><span style="color:#3498db;">'마이페이지 &gt; 내 정보 관리(오른쪽 위 톱니바퀴) &gt; 알림 설정'</span></a>에서 변경<br><br>
<br><br>
※ 앱 알림은 항목별로 ON/OFF 설정 가능합니다.<br><br>
(설정 리스트: 쇼핑/이벤트 혜택, 관심 브랜드 소식, 스냅, 활동)<br><br>
※ 알림 설정은 앱에서만 가능합니다.							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=292</div>
						</td>
					</tr>
										<tr>
					   <td style="border: none">17</td>
					   <td style="border: none" class="txt_contents"><a href="javascript:void(0)" onclick="viewContent('faq_294', '', ''); return false;">신규 회원 가입 이벤트(990원 이벤트)는 어떻게 참여할 수 있나요?</a></td>
					</tr>
					<tr id="faq_294" style="display: none;">
						<td style="border: none" class="faq_q">답변</td>
						<td style="border: none" class="faq_a">
							신규 회원 가입 후, 이벤트 상품 외 15,000원 이상 주문 시 이벤트 상품을 저렴한 가격(최저 990원부터)으로 구매하실 수 있는 이벤트입니다.<br><br>
<br><br>
※신규 회원 가입 후 6개월 내에 참여 가능합니다.<br><br>
<br><br>
<u><strong><a href="http://store.musinsa.com/app/content/s/usr/membership" target="_blank"><span style="color:#3498db;">이벤트 바로가기 (스토어 &gt; 이벤트 &gt; 990원 이벤트)</span></a></strong></u>							<div class="faq_url"><span>URL</span>http://store.musinsa.com/app/cs/faq/18?view_no=294</div>
						</td>
					</tr>
								   </tbody>
			</table>
"""



def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

def split_text(text_raw):
    ret = text_raw.replace("\n", "").replace("\t", "").split("  ")
    ret.remove("")
    return ret

def parse_answer(text_raws):
    ret = list()    
    for text_raw in text_raws:
        temp_record = dict()
        if text_raw == '':
            continue
        
        elif ' 번호' == text_raw:
            continue
        
        elif ' 내용' == text_raw:
            continue
        
        elif '답변' in text_raw:
            ret.append(text_raw)
        else:
            ret.append(text_raw)
    return ret
            

cleansing_text = split_text(cleanhtml(text_string))
cleansing_text = parse_answer(cleansing_text)
for idx, ele in enumerate(cleansing_text):
    print(ele)
