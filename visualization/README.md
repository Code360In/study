# 데이터 시각화 공부
# 시각화 
## 클린뷰티
![image](https://user-images.githubusercontent.com/47103479/128440835-218ce71a-d71e-42f3-9257-f865546c8805.png)
![image](https://user-images.githubusercontent.com/47103479/128440879-02e83d43-a232-4926-965f-fcc35ba1cb38.png)
![image](https://user-images.githubusercontent.com/47103479/128440906-e83cf6de-7116-4b23-80c8-ec8ca9f1f2cc.png)
![image](https://user-images.githubusercontent.com/47103479/128440921-0d070473-74af-4026-ab5b-3b05246d0c5f.png)
![image](https://user-images.githubusercontent.com/47103479/128440951-7dcee1f9-19b5-4cf0-a4fb-b9c42dda23d6.png)

```python
fig_satisfy = Tab()

pie_total =(
              Bar(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
               .add_xaxis(df['year'].tolist())
               .add_yaxis('', df['val'].tolist(), label_opts=opts.LabelOpts(position="right",formatter="{c}억"))
               .reversal_axis()
               .set_global_opts(title_opts=opts.TitleOpts(title="세계 비건 화장품 시장 성장 예측", 
                                                          #subtitle="마우스를 막대에 올려 정확한 수치를 확인해보세요!"
                                                          ),
                                yaxis_opts=opts.AxisOpts(name_location = "start")
                                #tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"))),"{}년도".format(t)
                                )
               )
fig_satisfy.add(pie_total,'홈뷰티')
fig_satisfy.render("pie_set_color1.html")
```
![image](https://user-images.githubusercontent.com/47103479/128532096-7f98d466-a13c-4097-96c9-d2753bc620f1.png)


# 필사 
- 데이터 시각화 필사를 하면서 공부하고있습니다.
(필사 자료 : https://jehyunlee.github.io/)

# 시각화필사_년도별 출생 및 수능
![image](https://user-images.githubusercontent.com/47103479/121812384-961a3400-cca2-11eb-8abb-7fe6e7581b5b.png)
![image](https://user-images.githubusercontent.com/47103479/121812390-987c8e00-cca2-11eb-9a41-4db4fdb3e0a7.png)


# 시각화필사_이중그래프

![image](https://user-images.githubusercontent.com/47103479/121811785-60744b80-cca0-11eb-8530-ca554dc06409.png)
![image](https://user-images.githubusercontent.com/47103479/121811788-6407d280-cca0-11eb-8307-439cbbd43520.png)
![image](https://user-images.githubusercontent.com/47103479/121811789-666a2c80-cca0-11eb-91fe-fc2c7e6a058e.png)

# 시각화 데이터들
![image](https://user-images.githubusercontent.com/47103479/121917005-a1876100-cd6f-11eb-8f36-4e32e7a59d63.png)
![image](https://user-images.githubusercontent.com/47103479/121917015-a3e9bb00-cd6f-11eb-9d22-45c1acb505ef.png)


# 시각화필사_matplotlib

![image](https://user-images.githubusercontent.com/47103479/121811745-420e5000-cca0-11eb-9252-801f6e98df0a.png)

# 시각화필사_matplotlib2

![image](https://user-images.githubusercontent.com/47103479/121811804-73871b80-cca0-11eb-957e-0ee89994e72b.png)
![image](https://user-images.githubusercontent.com/47103479/121811805-75e97580-cca0-11eb-8ceb-dc98355a3bb7.png)

# 시각화필사_Seaborn

![image](https://user-images.githubusercontent.com/47103479/121811687-1a1eec80-cca0-11eb-915b-87199a47b482.png)
![image](https://user-images.githubusercontent.com/47103479/121811668-10958480-cca0-11eb-8a4c-f1ba4e981559.png)
![image](https://user-images.githubusercontent.com/47103479/121811710-2a36cc00-cca0-11eb-885c-6bf4ccef38ba.png)

# watermark

![image](https://user-images.githubusercontent.com/47103479/121811597-cdd3ac80-cc9f-11eb-880c-06cdd5092f19.png)
