import random
import streamlit as st

def score_essay(essay):
    """Simple scoring function based on word count and basic structure."""
    word_count = len(essay.split())
    if word_count < 50:
        return "Score: 2/10 (Too short, needs more content)"
    elif 50 <= word_count < 150:
        return "Score: 5/10 (Average, try to elaborate more)"
    elif 150 <= word_count < 300:
        return "Score: 8/10 (Good effort, well-detailed)"
    else:
        return "Score: 10/10 (Excellent, comprehensive essay)"

def essay_writing():
    st.title("Essay Writing Practice")

    # Define subjects and corresponding essay topics with difficulty levels
    subjects = {
        "Literacy": {
            "easy": [
                "Why is literacy important for personal development?",
                "Why is literacy important for personal development?",
                "How can schools contribute to improving literacy rates in India?",
                "What are the benefits of literacy for children?",
                "How does literacy contribute to a nation’s economic growth?",
                "How does literacy improve social well-being?",
                "What role does technology play in promoting literacy?",
                "What are the challenges of achieving universal literacy in India?",
                "How does adult literacy impact family life?",
                "What role does government play in improving literacy rates?",
                "Why is literacy important for women’s empowerment?",
                "How can libraries help improve literacy in rural areas?",
                "What is the impact of illiteracy on society?",
                "How does literacy affect health awareness?",
                "What is the importance of early childhood education in literacy development?",
                "How does literacy affect political participation?"
                "How can schools contribute to improving literacy rates in India?",
                "What are the benefits of literacy for children?"
            ],
            "medium": [
                "Challenges faced in promoting literacy in India.",
                "The impact of digital literacy on employment opportunities",
                "How can India reduce the gender gap in literacy?",
                "What role do NGOs play in improving literacy in rural India?",
                "How can technology be used to enhance literacy in remote areas?",
                "How does literacy impact social mobility in India?",
                "What are the barriers to achieving literacy among marginalized communities?",
                "How do different languages affect literacy development in India?",
                "What is the relationship between literacy and employment opportunities?",
                "What are the challenges in improving adult literacy rates in India?",
                "How can government policies promote literacy in tribal areas?",
                "What are the impacts of poor literacy on health outcomes?",
                "What role do teachers play in improving literacy rates?",
                "How can literacy programs be made more effective?",
                "How does literacy contribute to reducing poverty?",
                "What are the socio-economic benefits of improving literacy in urban slums?",
                "How do literacy rates impact the economic development of a nation?",
                "The impact of digital literacy on employment opportunities.",
                "How can India reduce the gender gap in literacy?"
            ],
            "advanced": [
                "How does literacy in a digital age influence social and political participation?",
                "What are the long-term economic consequences of low literacy rates in India?",
                "Can literacy alone contribute to the development of a knowledge-based economy?",
                "How does literacy in rural areas impact India's overall economic growth?",
                "What are the implications of illiteracy on democratic governance in India?",
                "How can India address the challenges of functional literacy?",
                "To what extent does illiteracy hinder technological adoption in India?",
                "How can India’s education system balance quality literacy education with universal access?",
                "What is the role of gender-sensitive literacy programs in empowering women in rural India?",
                "How can the media contribute to promoting literacy across different age groups?",
                "What are the implications of digital literacy on global competitiveness?",
                "How does the political will of the Indian government affect literacy outcomes?",
                "What are the ethical concerns in promoting literacy through standardized methods?",
                "How does the quality of education impact the future literacy rate in India?",
                "What is the role of international collaboration in improving literacy in developing countries?"
            ]
        },
        "Gender Equality": {
            "easy": [
                "The role of women in building a sustainable society.",
                "The importance of gender equality in modern societies.",
                "What are the basic principles of gender equality?",
                "How does gender equality benefit society?",
                "What are the effects of gender inequality on women’s health?",
                "How can education promote gender equality?",
                "Why is gender equality important in the workplace?",
                "What role does government play in ensuring gender equality?",
                "How does gender equality impact economic development?",
                "What is the role of media in promoting gender equality?",
                "How can men be involved in promoting gender equality?",
                "Why is equal access to education important for both genders?",
                "What is the significance of women’s participation in politics?",
                "How can gender-based violence be prevented?",
                "What are the main barriers to gender equality in India?",
                "How does gender equality contribute to peace and security?",
                "Why is gender equality a fundamental human right?"

            ],
            "medium": [
                "The challenges in achieving gender parity in the workplace.",
                "What are the challenges to achieving gender equality in rural India?",
                "How do cultural practices affect gender equality in Indian society?",
                "How can gender equality contribute to economic growth in developing countries?",
                "What are the effects of gender inequality on children’s education?",
                "How can gender equality be integrated into corporate policies?",
                "What are the challenges faced by women in achieving economic independence?",
                "How does gender equality contribute to reducing poverty?",
                "What is the importance of political participation of women in ensuring gender equality?",
                "How can India tackle the gender pay gap?",
                "How can access to technology improve gender equality?",
                "What is the role of women in rural development?",
                "How can legal reforms help in achieving gender equality?",
                "What are the barriers to achieving gender equality in higher education?",
                "How does gender inequality in health affect overall development?",
                "What are the effects of gender stereotypes in shaping career choices?",
                "Women’s representation in politics: A global perspective."
            ],
            "advanced": [
                "The intersection of gender equality and economic growth.",
                "How can India address the deeply ingrained cultural and societal norms that perpetuate gender inequality?",
                "What are the political, social, and economic consequences of gender inequality in India?",
                "How can India achieve gender parity in leadership roles?",
                "What is the role of gender quotas in promoting equality in political institutions?",
                "To what extent does gender-based violence undermine India’s progress toward gender equality?",
                "How do globalization and technological advancement affect gender equality?",
                "What are the structural barriers that prevent women’s economic empowerment in India?",
                "What are the long-term effects of gender inequality on economic development?",
                "How can international organizations assist in achieving gender equality in developing countries?",
                "How do intersectional issues such as caste and class compound gender inequality in India?",
                "What role does education play in transforming gender norms in rural India?",
                "How can gender equality be ensured within the framework of Indian multiculturalism?",
                "How does gender inequality affect India’s international competitiveness?",
                "What are the implications of gender inequality on India’s demographic profile?",
                "How can India reconcile traditional family structures with the demands for gender equality?",
                "The role of cultural norms in shaping gender roles."
            ]
        },
        "Environment/Urbanization": {
            "easy": [
                "The impact of urbanization on local ecosystems.",
                "What are the benefits of environmental conservation?",
                "Why is it important to protect endangered species?",
                "What role do citizens play in protecting the environment?",
                "How does pollution affect human health?",
                "What are the environmental impacts of deforestation?",
                "How can urbanization be made sustainable?",
                "What is the importance of recycling in protecting the environment?",
                "How can government policies help in controlling pollution?",
                "Why is waste management important in urban areas?",
                "What are the effects of air pollution on urban populations?",
                "How do green spaces in cities contribute to the environment?",
                "What are the economic benefits of sustainable urbanization?",
                "How does climate change affect the global environment?",
                "What are the advantages of renewable energy sources?",
                "Why should we promote public transportation in urban areas?",
                "The importance of green spaces in urban environments."
            ],
            "medium": [
                "The challenges of managing waste in rapidly urbanizing cities.",
                "What challenges do cities face in becoming environmentally sustainable?",
                "How does urban sprawl contribute to environmental degradation?",
                "What role does technology play in creating sustainable cities?",
                "What are the social implications of climate change in urban areas?",
                "How can urbanization contribute to the loss of biodiversity?",
                "What is the impact of industrialization on environmental sustainability?",
                "How can India’s rapidly growing cities address waste management challenges?",
                "What are the environmental impacts of large-scale agricultural practices?",
                "How do urban planning policies affect environmental conservation?",
                "How can India reduce its carbon footprint through urban planning?",
                "What are the environmental challenges posed by water scarcity in urban areas?",
                "What role do urban agriculture and green roofs play in sustainable cities?",
                "How can public-private partnerships promote sustainable development?",
                "What are the effects of deforestation on climate change?",
                "How can cities mitigate the environmental impact of transportation?",
                "The role of sustainable urbanization in reducing environmental impact."
            ],
            "advanced": [
                "Smart cities and their role in sustainable development.",
                "What is the role of urbanization in exacerbating global environmental challenges?",
                "How can India balance economic growth with environmental conservation in its urban areas?",
                "What are the implications of rapid urbanization on India’s natural resources?",
                "How does climate change affect migration patterns, especially in coastal regions?",
                "What is the relationship between poverty and environmental degradation in urban areas?",
                "What policies should the Indian government adopt to address the environmental challenges of megacities?",
                "How does the built environment in cities contribute to global warming?",
                "How can green urbanism be integrated into India’s urban planning?",
                "What are the economic and environmental implications of large-scale urbanization in India?",
                "How can India’s energy sector transition towards sustainability while meeting growing demands?",
                "How can cities adapt to the challenges posed by climate change?",
                "What are the long-term environmental consequences of unregulated industrial growth in urban areas?",
                "How does urban poverty contribute to environmental degradation?",
                "What role does sustainable agriculture play in mitigating climate change?",
                "How can international collaborations address urbanization and environmental concerns?",
                "The ethical implications of urbanization on rural populations."
            ]
        },
        "Economic Growth": {
            "easy": [  
                "What are the key factors that contribute to economic growth?",
            	"How does education impact a nation’s economic growth?",
            	"What role does entrepreneurship play in economic growth?",
            	"How does access to technology promote economic development?",
            	"Why is infrastructure important for economic growth?",
	            "What is the significance of foreign trade in economic growth?",
                "How does investment in health impact a country’s economy?",
	            "Why is the agriculture sector important for economic growth in developing countries?",
             	"What are the benefits of a stable political environment for economic growth?",
       	        "How does a strong financial sector contribute to economic development?",
                "How does job creation help promote economic growth?",
                "What are the impacts of a growing middle class on economic development?",
                "Why is good governance essential for economic growth?",
	            "What role does innovation play in economic growth?",
            	"How does government spending influence economic growth?"
            ],
            "medium": [
            	"How does corruption affect a country's economic growth?",
            	"What are the challenges faced by developing countries in achieving sustainable economic growth?",
            	"How does economic growth affect income inequality?",
            	"What is the relationship between population growth and economic development?",
            	"How can environmental sustainability be integrated with economic growth?",
            	"What are the effects of high inflation on economic growth?",
                "How do trade wars and protectionism impact economic growth?",
	            "What role do international financial institutions play in promoting economic growth?",
	            "How does income distribution affect economic development?",
            	"How does technological advancement contribute to economic growth?",
             	"What is the impact of foreign direct investment (FDI) on economic growth?",
                "How can India ensure inclusive growth for all sections of society?",
                "What are the challenges of achieving high growth in a post-pandemic world?",
                "How can economic growth be maintained while addressing environmental concerns?",
             	"How do government policies impact economic growth in emerging economies?"
            ],
            "advanced": [
            	"How can India balance the pursuit of economic growth with the need for environmental sustainability?",
	            "What are the implications of rising economic inequality for long-term growth?",
	            "How can India’s economy transition from a predominantly agrarian economy to an industrialized one?",
            	"How does global economic integration affect India’s growth prospects?",
            	"What is the role of innovation and research and development in sustaining economic growth?",
            	"How can India ensure that its economic growth is inclusive and equitable?",
            	"What are the economic consequences of India’s increasing reliance on foreign capital?",
            	"How can the Indian government foster a conducive environment for high-tech industries to thrive?",
            	"How does the political economy influence economic growth in India?",
                "What is the relationship between economic growth and human development?",
            	"How can India mitigate the risks associated with economic growth, such as over-reliance on certain sectors?",
            	"What are the challenges of achieving sustainable growth in urban areas?",
            	"How can India address the economic consequences of climate change while fostering growth?",
            	"What is the role of social protection schemes in ensuring that growth is inclusive?",
            	"How can India integrate the informal economy into the formal growth process?"

            ]
        },
        "Technology": {
            "easy": [
                "What are the benefits of using technology in everyday life?",
                "How does technology improve communication?",
                "How has technology transformed the education sector?",
                "What is the impact of mobile technology on society?",
                "Why is technology important for business growth?",
                "How does technology enhance healthcare services?",
                "How can technology be used to improve the quality of education?",
                "What role does technology play in environmental protection?",
                "What is the impact of technology on the job market?",
                "How does technology improve transportation?",
                "What are the advantages of digital banking?",
                "How has technology changed the way we work?",
                "How does social media impact communication and relationships?",
                "Why is access to technology important for rural areas?",
                "How does technology facilitate government services?"

            ],
            "medium": [
                "How can India leverage technology to achieve sustainable economic growth?"
                "What are the challenges of digital divide in India?",
                "How does technology affect privacy and security?",
                "What are the ethical implications of artificial intelligence?",
                "How can technology help in reducing poverty and inequality?",
                "What is the role of technology in improving public healthcare?",
                "How can technology enhance governance and transparency?",
                "How can technology be used to solve environmental problems?",
                "What are the impacts of automation and robotics on employment?",
                "How can technology transform agriculture in India?",
                "What role does technology play in shaping modern education?",
                "How can India ensure that its workforce is prepared for a tech-driven future?",
                "How can the government ensure equal access to technology for all citizens?",
                "What are the implications of cybercrime in an increasingly digital world?",
                "How does technology influence cultural exchange and globalization?"

            ],
            "advanced": [
                "How can India lead the world in innovation while addressing its unique socio-economic challenges?",
                "What are the political, economic, and social challenges of widespread automation?",
                "How can India ensure that its digital transformation benefits all sectors of society?",
                "What are the implications of artificial intelligence on traditional job markets?",
                "How can technology be used to achieve sustainable development goals?",
                "What are the risks of over-reliance on technology in developing countries?",
                "How can India harness technology to bridge the gap between urban and rural areas?",
                "What is the role of technology in managing global health crises, such as pandemics?",
                "What are the ethical challenges posed by big data and machine learning?",
                "How can India protect its digital sovereignty while integrating with global tech platforms?",
                "What role does intellectual property play in technology innovation?",
                "How can digital technologies be utilized to improve governance in democratic nations?",
                "How do emerging technologies affect global power dynamics?",
                "What is the role of technology in promoting digital democracy?",
                "How can India address the environmental impact of its tech industry?"

            ]
        },
        "Religion": {
            "easy": [
               "What is the role of religion in shaping moral values?",
               "How does religion influence daily life?",
               "What is the significance of religious festivals in Indian society?",
               "How do different religions promote peace and harmony?",
               "Why is religious tolerance important in a diverse society?",
               "How do religious beliefs influence cultural practices?",
               "What is the impact of religion on family life?",
               "How does religion contribute to community welfare?",
               "How can interfaith dialogue promote understanding and peace?",
               "What role does religion play in personal identity?",
               "How does religion affect the legal system in India?",
               "How can religious teachings influence social behavior?",
               "What is the importance of religious freedom in a democratic society?",
               "How does religion promote charity and social service?",
               "Why is the study of religion important in education?"
            ],
             "medium": [
               "How does religion affect political decisions and governance?",
               "What is the relationship between religion and human rights?",
               "How can religious institutions contribute to social justice?",
               "How does secularism promote religious freedom?",
               "What are the challenges of managing religious diversity in India?",
               "How does religion influence gender roles in society?",
               "What role does religion play in conflicts around the world?",
               "How can religion be used to promote environmental sustainability?",
               "How does the caste system intertwine with religion in India?",
               "What are the ethical dilemmas in religious practices?",
               "How does religious nationalism affect social cohesion?",
               "How can religious teachings be reconciled with modern scientific understanding?",
               "What is the role of religion in the development of ethics in society?",
               "How can religious institutions foster economic development?",
               "How do religious minorities protect their rights in a secular country?"
            ],
            "advanced": [
               "What is the role of religion in shaping the global political order?",
               "How do religious movements impact social and political change?",
               "What are the challenges of maintaining religious pluralism in a modern society?",
               "How can religion contribute to sustainable development goals?",
               "What are the economic impacts of religion on global trade and commerce?",
               "How does religion affect the relationship between the state and individual freedoms?",
               "What is the role of religion in post-colonial societies?",
               "How can religious extremism be addressed without infringing on individual freedoms?",
               "What are the challenges of religious conversion in multicultural societies?",
               "How can secularism and religion coexist in a diverse society?",
               "How does religion influence global conflicts and peace-building efforts?",
               "What is the impact of globalization on religious beliefs and practices?",
               "How does religious identity affect international relations?",
               "What are the ethical challenges posed by religious fundamentalism?",
               "How can interfaith dialogue contribute to global peace?"
            ]
        },
        "Federalism/Decentralization": {
          
            "easy": [
               "What is federalism?",
               "How does federalism benefit a country like India?",
               "What is decentralization in governance?",
               "How does decentralization improve service delivery in rural areas?",
               "What are the advantages of decentralizing power to local governments?",
               "How does federalism help in managing diverse cultures?",
               "What is the role of states in a federal system?",
               "What is the relationship between state governments and central governments?",
               "How does federalism help in managing resources across states?",
               "What are the challenges faced by local governments in a decentralized system?",
               "How does federalism promote democratic participation?",
               "How does federalism accommodate regional differences?",
               "Why is decentralization important for grassroots development?",
               "What is the role of Panchayats and Municipalities in decentralization?",
               "How can decentralization lead to improved accountability in governance?"
            ],
             "medium": [
                "How does federalism impact economic policies in India?",
                "What are the challenges of implementing federalism in a diverse society?",
                "How does decentralization affect the distribution of resources in India?",
                "How does federalism impact the political relationship between the center and states?",
                "What role does federalism play in conflict resolution in multi-ethnic societies?",
                "How can decentralization help in reducing corruption?",
                "What are the effects of decentralization on local governance?",
                "How does federalism ensure political stability in large countries?",
                "How does the federal structure of India support the principle of unity in diversity?",
                "What is the role of the Finance Commission in a federal system?",
                "How does decentralization improve public services like education and healthcare?",
                "What challenges does federalism pose to national security?",
                "What are the advantages and disadvantages of having a strong central government versus a decentralized government?",
                "How does federalism influence the decision-making process in the Indian government?",
                "How can decentralized governance improve the participation of marginalized groups?"
            ],
            "advanced": [
                "How can India’s federal system be reformed to ensure better cooperation between the center and states?",
                "What are the implications of financial decentralization in India’s federal structure?",
                "How does the distribution of power between the center and states affect national policies?",
                "What are the challenges of federalism in managing national integration?",
                "How can federalism in India be used to address regional disparities?",
                "What are the constitutional and legal challenges to decentralization in India?",
                "How does federalism impact national economic policies, particularly in a globalized world?",
                "How does decentralization contribute to the empowerment of women and marginalized communities?",
                "What are the consequences of weak federal systems on a country’s political stability?",
                "How can federalism be reconciled with the demands for regional autonomy?",
                "What is the impact of federalism on India’s foreign policy?",
                "How can India manage the tension between regional aspirations and national unity through federalism?",
                "What are the ethical considerations in the distribution of powers between the central and state governments?",
                "What role does federalism play in conflict management and peace-building in insurgency-prone areas?",
                "How does the judiciary influence the functioning of federalism in India?"
            ]
        },
         "Health": {
            "easy": [
               "Why is healthcare important for a nation?",
               "What are the basic elements of a good healthcare system?",
               "How does access to healthcare contribute to a better quality of life?",
               "What are the common health problems faced by India?",
               "How does sanitation impact public health?",
               "Why is vaccination important for public health?",
               "How does nutrition affect overall health?",
               "Why are mental health issues important to address in healthcare?",
               "How can public awareness campaigns help in improving public health?",
               "What role does the government play in providing healthcare services?",
               "What is the role of primary healthcare in health promotion?",
               "How do hospitals contribute to healthcare?",
               "What is the importance of preventive healthcare?",
               "What is the role of health insurance in promoting healthcare?",
               "Why is maternal health a critical part of healthcare?"
            ],
            "medium": [
               "How can healthcare be made more accessible in rural India?",
               "What are the challenges of providing affordable healthcare in India?",
               "What are the advantages and disadvantages of private versus public healthcare?",
               "How does air pollution affect public health?",
               "How can the government improve mental healthcare in India?",
               "How does sanitation affect public health in urban and rural areas?",
               "What are the benefits of universal healthcare in India?",
               "What are the key challenges faced by India’s healthcare system?",
               "How can India address the problem of malnutrition?",
               "What role does telemedicine play in enhancing healthcare access?",
               "How does lifestyle affect public health in modern society?",
               "What is the importance of research in improving healthcare?",
               "How can public-private partnerships improve healthcare in India?",
               "How can healthcare systems better prepare for pandemics?",
               "What is the impact of technology on healthcare services?"
           ],
            "advanced": [
               "What are the policy challenges in ensuring universal healthcare in India?",
               "How does the social determinants of health model inform healthcare policies?",
               "What role does biotechnology play in shaping the future of healthcare?",
               "How can India address the healthcare needs of its aging population?",
               "How can healthcare systems be reformed to meet the challenges posed by non-communicable diseases?",
               "What are the ethical concerns in implementing a universal health insurance scheme?",
               "What are the challenges of addressing health disparities in a country like India?",
               "How can India reduce the burden of communicable diseases like tuberculosis and malaria?",
               "How can India address the issue of medical brain drain?",
               "How does healthcare expenditure impact economic growth?",
               "What are the challenges in integrating traditional and modern healthcare systems?",
               "What role does technology play in enhancing the efficiency of healthcare delivery?",
               "How can India tackle the growing problem of antimicrobial resistance?",
               "What is the role of health governance and policy in ensuring quality healthcare?",
               "How can the Indian healthcare system adapt to the challenges posed by urbanization?"
            ]
        },
        "Poverty": {
            "easy": [
                "What is poverty?",
                "How does poverty affect education?",
                "How does poverty impact a person’s health?",
                "What are the causes of poverty in India?",
                "How does access to clean water help in reducing poverty?",
                "Why is poverty a barrier to social development?",
                "How can access to employment reduce poverty?",
                "What role do government schemes play in poverty alleviation?",
                "What are the impacts of poverty on children?",
                "How does poor nutrition contribute to poverty?",
                "What is the role of education in reducing poverty?",
                "How does the lack of infrastructure contribute to poverty?",
                "Why is poverty often linked to social inequality?",
                "How does poverty affect family dynamics?",
                "How does poverty impact mental health?",
                "The role of education in alleviating poverty.",
                "How microfinance can help reduce poverty in rural areas."
            ],
            "medium": [
                "The impact of unemployment on poverty levels.",
                "What are the most effective poverty alleviation programs in India?",
                "How can rural development help reduce poverty?",
                "What is the relationship between poverty and unemployment?",
                "How does poverty affect economic development?",
                "What role does income inequality play in exacerbating poverty?",
                "How can access to credit help in poverty reduction?",
                "What are the main challenges in eradicating poverty in urban areas?",
                "How do economic crises worsen poverty in developing countries?",
                "How can government policies ensure inclusive growth to reduce poverty?",
                "What is the connection between poverty and crime?",
                "How does migration from rural to urban areas impact poverty?",
                "What are the social implications of poverty in India?",
                "How can microfinance contribute to poverty alleviation?",
                "What is the role of women’s empowerment in reducing poverty?",
                "How does the lack of affordable healthcare contribute to poverty?",
                "The role of social security programs in poverty reduction."
            ],
            "advanced": [
                "The role of economic inequality in perpetuating poverty.",
                "How can India's economic growth be made more inclusive to reduce poverty?",
                "What are the challenges of implementing a universal basic income in India?",
                "How can poverty be tackled through structural reforms in agriculture?",
                "What role does international aid play in alleviating poverty?",	 
                "How does caste-based inequality contribute to poverty in India?",
                "What are the links between poverty and environmental sustainability?",
                "How can social protection programs be designed to effectively reduce poverty?",
                "What are the economic and social costs of poverty in India?",
                "How can technological innovations contribute to poverty reduction?",
                "How does poverty influence political participation and social stability?",
                "What are the long-term effects of poverty on a nation’s development?",
                "How can global trade policies be restructured to reduce poverty in developing countries?",
                "What is the relationship between poverty and educational attainment in India?",
                "How can inclusive economic growth ensure better poverty outcomes?",
                "How can access to affordable housing address poverty?",               
               "How global trade policies affect poverty in developing countries."
            ]
        },
        "Judiciary": {
            "easy": [
                "What is the role of the judiciary in a democracy?",
                "What is the importance of an independent judiciary?",
                "What is the difference between criminal and civil law?",
                "How does the judiciary protect fundamental rights?",
                "What are the key functions of a court of law?",
                "What is the role of judges in the judicial system?",
                "Why is the rule of law important in governance?",
                "How does the judiciary maintain checks and balances in government?",
                "What is the importance of the Supreme Court in India?",
                "What are public interest litigations (PILs) in the Indian judiciary?",
                "How does the judiciary ensure justice for all citizens?",
                "What is the role of the judiciary in interpreting the constitution?",
                "How do courts ensure the enforcement of laws?",
                "What is the role of the lower judiciary in India?",
                "What is judicial review?",
                "The role of the judiciary in ensuring justice.",
                "The importance of judicial independence in democracy."
            ],
            "medium": [
                "Judicial activism in India: Pros and cons.",
                "What challenges does the Indian judiciary face in ensuring timely justice?",
                "How does the judiciary address social justice issues in India?",
                "How does the judiciary play a role in protecting minority rights?",
                "What is the impact of judicial activism on Indian democracy?",
                "What are the implications of the increasing backlog of cases in Indian courts?",
                "How can judicial reforms improve the delivery of justice in India?",
                "What role does the judiciary play in protecting the environment?",
                "What is the concept of judicial independence, and why is it important?",
                "How does the judiciary play a role in upholding secularism in India?",
                "How do courts balance individual rights with national security concerns?",
                "What role do high courts play in the Indian judicial system?",
                "How does the judiciary ensure the protection of the rights of women?",
                "How does the judiciary handle cases related to corruption?",
                "What are the challenges of ensuring judicial accountability?",
                "How can the judiciary ensure that all citizens have access to justice?",
                "The role of the judiciary in upholding human rights."
            ],
            "advanced": [
                "The challenges of judicial reforms in India.",
                "What reforms are necessary to ensure greater efficiency in the Indian judicial system?",
                "What role does judicial review play in the interpretation of the Constitution?",
                "How can the judiciary balance judicial independence with accountability?",
                "How does the judiciary contribute to the socio-economic development of India?",
                "What are the ethical challenges faced by the judiciary in the delivery of justice?",
                "What is the role of the judiciary in protecting democratic values in India?",
                "How can the judiciary address the challenges of judicial overreach?",
                "What is the relationship between the judiciary and executive in India?",
                "How can India address the issue of judicial corruption?",
                "How can alternative dispute resolution (ADR) mechanisms ease the burden on courts?",
                "What are the constitutional challenges in ensuring the independence of the judiciary?",
                "How does the judiciary contribute to the protection of environmental rights?",
                "What role do international courts play in shaping domestic judicial systems?",
                "How can the judiciary respond to the challenges of hate speech and social unrest?",
                "What is the impact of technological advancements on the functioning of the judiciary?",
                "The relationship between judiciary and executive in a democratic system."
            ]
        },
        "Culture": {
            "easy": [
                "The significance of cultural heritage in modern society.",
                "What is culture?",
                "How does culture shape society?",
                "Why is cultural diversity important?",
                "How does culture influence our values and beliefs?",
                "What role does art play in culture?",
                "What is the importance of festivals in cultural traditions?",
                "How does language shape cultural identity?",
                "Why is music an important part of culture?",
                "How do cultural practices influence daily life?",
                "How does the media influence culture?",
                "What is the role of religion in shaping culture?",
                "How do cultural practices differ across regions in India?",
                "Why is preserving cultural heritage important?",
                "What are the influences of globalization on local cultures?",
                "What is the role of education in promoting cultural awareness?",
                "The impact of globalization on traditional cultures."
            ],
            "medium": [
                "Cultural diversity and its impact on social harmony.",
                "How do cultural values influence social behavior in India?",
                "What are the challenges of preserving indigenous cultures in a globalized world?",
                "How can cultural diversity enhance national development?",
                "What role does literature play in preserving culture?",
                "How does migration impact cultural identity?",
                "How does technology influence cultural expressions?",
                "What role does cinema play in reflecting and shaping culture?",
                "How does globalization impact traditional cultural practices?",
                "What is the role of museums in preserving cultural heritage?",
                "How do cultural practices affect gender roles in society?",
                "What is the significance of folk traditions in modern culture?",
                "How can intercultural exchange promote peace and understanding?",
                "What role does food play in cultural identity?",
                "How does cultural appropriation affect cultural preservation?",
                "How does cultural pluralism contribute to social harmony?",
                "The role of art and literature in shaping cultural identity."
            ],
            "advanced": [
                "The role of cultural diplomacy in international relations.",
                "How does the tension between modernity and tradition influence cultural evolution?",
                "What are the impacts of cultural homogenization on indigenous cultures?",
                "How can cultural diplomacy improve international relations?",
                "What is the role of culture in nation-building?",
                "How does culture influence the political and economic landscape of a country?",
                "How can cultural industries contribute to economic development?",
                "What are the challenges of balancing cultural preservation with development?",
                "What is the impact of post-colonialism on the cultural identity of nations?",
                "How can India manage the intersection of culture and nationalism?",
                "What is the role of cultural institutions in promoting social cohesion?",
                "How do global media influence local cultures?",
                "How can cultural tourism impact the preservation of heritage sites?",
                "How does the commodification of culture affect its authenticity?",
                "How does culture shape the perception of power and authority?",
                "What is the role of culture in addressing social inequalities?",
                "The challenges of preserving cultural heritage in the face of modernization."
            ]
        },
        "Agriculture": {
            "easy": [
                "What is agriculture?",
                "Why is agriculture important for a country’s economy?",
                "What are the main types of agriculture?",
                "How do farmers contribute to the economy?",
                "What is the role of irrigation in agriculture?",
                "Why is crop rotation important in agriculture?",
                "What are the main challenges faced by farmers in India?",
                "What are the benefits of organic farming?",
                "How does the monsoon season affect agriculture?",
                "What is the importance of soil fertility for farming?",
                "What are the main crops grown in India?",
                "What is the role of agricultural machinery in modern farming?",
                "How does agriculture impact the environment?",
                "What is the significance of the Green Revolution?",
                "What are the advantages of sustainable farming practices?"
            ],
            "medium": [
                "How does agriculture contribute to the development of rural areas?",
                "What are the challenges of agricultural diversification in India?",
                "How do government policies impact the agricultural sector?",
                "What are the environmental impacts of modern farming practices?",
                "How does climate change affect agricultural productivity?",
                "What is the role of technology in modernizing agriculture?",
                "How can water scarcity be managed in agriculture?",
                "What are the advantages and disadvantages of GM crops?",
                "What are the economic implications of agricultural subsidies?",
                "How does agriculture contribute to food security?",
                "What are the challenges faced by small-scale farmers?",
                "How can agriculture address the problem of rural poverty?",
                "What role do agricultural cooperatives play in rural development?",
                "How does the agricultural supply chain function in India?",
                "What are the effects of global trade policies on Indian agriculture?"
            ],
            "advanced": [
                "What reforms are needed to ensure sustainable agricultural growth in India?",
                "How can agricultural diversification improve rural livelihoods?",
                "How can India manage the increasing demand for food in a growing population?",
                "What is the role of agriculture in mitigating climate change?",
                "How can India balance agricultural growth with environmental sustainability?",
                "What are the challenges of integrating agro-based industries into rural economies?",
                "How can agricultural policies promote both productivity and sustainability?",
                "What role do farmers' protests play in shaping agricultural policies?",
                "How does agricultural insurance contribute to risk management in farming?",
                "How can agricultural research and innovation support food security?",
                "What is the impact of land reform policies on agricultural productivity?",
                "What are the prospects of agroforestry in India’s agricultural future?",
                "How can precision farming techniques improve agricultural efficiency?",
                "What role does rural infrastructure play in agricultural development?",
                "How can India reduce its dependency on monsoon-driven agriculture?"
            ]
        },
        "Democracy": {
            "easy": [
                "What is democracy?",
                "Why is voting important in a democracy?",
                "What are the fundamental principles of democracy?",
                "How does democracy differ from autocracy?",
                "What role does the media play in a democracy?",
                "Why is freedom of speech important in a democracy?",
                "What is the role of political parties in a democracy?",
                "Why is equal representation essential in a democracy?",
                "What is the significance of free and fair elections?",
                "What is the relationship between democracy and human rights?",
                "How does democracy ensure the participation of citizens?",
                "Why is the rule of law important in a democracy?",
                "What is the significance of separation of powers in a democracy?",
                "What role do civil society organizations play in a democracy?",
                "How does democracy promote social justice?"
            ],
            "medium": [
                "How does democracy contribute to national integration?",
                "What are the challenges faced by democracies in the modern world?",
                "How does democracy support economic development?",
                "What are the risks of populism in a democracy?",
                "How does democracy balance individual freedom with social order?",
                "What is the role of the judiciary in safeguarding democracy?",
                "How does democratic governance ensure accountability?",
                "What is the relationship between democracy and development?",
                "How does decentralization strengthen democracy?",
                "What challenges does India face in maintaining democratic principles?",
                "How do international organizations promote democracy?",
                "What role does education play in sustaining democracy?",
                "How can technology influence democratic processes?",
                "What are the ethical dilemmas in electoral politics?",
                "How do democratic principles impact governance in multicultural societies?"
            ],
            "advanced": [
                "How can democracy be reformed to address the challenges of political polarization?",
                "What role does a vibrant opposition play in strengthening democracy?",
                "How can democracies balance the tension between national security and individual rights?",
                "What are the implications of digital democracy for political engagement?",
                "How does democracy address the issue of social inequality?",
                "How do constitutional amendments impact the functioning of democracy?",
                "What are the challenges of implementing direct democracy in large nations?",
                "How can the electoral system be reformed to ensure better representation in democracies?",
                "What is the relationship between democracy and the protection of minority rights?",
                "How can democratic societies address the challenges posed by authoritarianism?",
                "What is the role of civil liberties in maintaining democratic governance?",
                "How can democratic governments ensure transparency and accountability in governance?",
                "What is the role of democracy in conflict resolution?",
                "How does democracy ensure the protection of human dignity and freedom?",
                "What role do international laws and norms play in promoting democracy?"
            ]
        },
        "Economics": {
            "easy": [
                "What is economics?",
                "What are the basic principles of economics?",
                "What is the difference between microeconomics and macroeconomics?",
                "How do supply and demand determine prices?",
                "What is inflation?",
                "What is GDP?",
                "Why is saving important in an economy?",
                "How does government taxation impact the economy?",
                "What is the role of money in the economy?",
                "What is a market economy?",
                "What is a command economy?",
                "How do businesses contribute to the economy?",
                "What is the role of banks in the economy?",
                "How does trade benefit an economy?",
                "What is unemployment?"
            ],
            "medium": [
                "How does inflation affect purchasing power?",
                "What are the impacts of fiscal policies on economic growth?",
                "How does a country’s monetary policy affect inflation?",
                "What are the different types of unemployment?",
                "What is the significance of foreign direct investment (FDI) for an economy?",
                "How do interest rates influence economic activities?",
                "What is the relationship between economic growth and environmental sustainability?",
                "How does economic globalization impact local economies?",
                "What is the role of central banks in controlling inflation?",
                "How does international trade impact domestic industries?",
                "What is the significance of public debt in managing an economy?",
                "How can government policies mitigate economic recessions?",
                "How does consumer confidence influence economic decisions?",
                "What are the effects of tariffs on international trade?",
                "How do exchange rates impact the economy?"
            ],
            "advanced": [
                "How can fiscal and monetary policies be harmonized to ensure economic stability?",
                "What are the economic implications of an aging population?",
                "How can economic growth be made more inclusive?",
                "What role does economic inequality play in long-term economic development?",
                "How do technological advancements shape the future of global economies?",
                "What are the challenges of managing a mixed economy?",
                "What is the role of economic theory in policy-making?",
                "How does economic liberalization affect developing countries?",
                "What are the challenges of managing a large informal economy?",
                "How can sustainable economic development be achieved in the context of climate change?",
                "What are the economic consequences of trade wars?",
                "How does foreign exchange intervention affect a nation’s economy?",
                "What is the impact of automation on employment and economic productivity?",
                "How can governments manage economic volatility due to external shocks?",
                "What are the ethical implications of economic growth policies?"
            ]
        }
    }

    # Subject selection
    selected_subject = st.selectbox("Select a subject:", list(subjects.keys()))

    # Difficulty level selection
    difficulty_level = st.selectbox("Select a difficulty level:", ["easy", "medium", "advanced"])

    # Generate random essay topic
    topics = subjects[selected_subject][difficulty_level]
    random_topic = random.choice(topics)

    st.write(f"**Random Topic:** {random_topic}")

    # Text area for essay writing
    essay = st.text_area("Write your essay below:")

    # Submit button to evaluate
    if st.button("Submit and Evaluate"):
        if essay.strip():
            score = score_essay(essay)
            st.write(f"### Your Essay Score: {score}")
        else:
            st.write("Please write your essay before submitting.")

# Run the app
if __name__ == "__main__":
    essay_writing()
