from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class BabyLearningMama(VoiceoverScene):
    def construct(self):
        self.camera.background_color = "#FFB6C1"
        self.set_speech_service(GTTSService(lang="zh-CN"))

        # 创建角色
        mom = Text("妈妈", font="SimSun",color= BLACK).scale(1.5).to_edge(UP)
        baby = Text("宝宝", font="SimSun" ,color=BLACK).scale(1.2).to_edge(DOWN)
        baby.shift(UP)
        # 创建发音文本
        momPronunciation = Text("mā mā", font="Arial",color=BLACK).scale(0.8).next_to(mom, DOWN)
        babyPronunciation = Text("bǎo bǎo", font="Arial",color=BLACK).scale(0.8).next_to(baby, DOWN)



        # 动画展示
        # self.play(Write(mom))
        # self.play(Write(momPronunciation))
        # self.wait(1)
        self.play(Write(mom))
        self.wait(1)

        with self.voiceover(text="妈妈") as tracker:
            self.play(Write(momPronunciation), run_time=tracker.duration)

        # self.add_sound("mother.mp3")
        self.wait(2)
   
        self.play(Write(baby))
        self.play(Write(babyPronunciation))
        self.wait(1)


        heart = ParametricFunction(
                lambda t: np.array([
                    16 * np.sin(t)**3,
                    13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t),
                    0
                ]),
                t_range = np.array([0, TAU]),
                color = RED
            ).scale(0.1)
        
        heart.move_to(ORIGIN)
        # 显示心形，表示爱
        self.play(Create(heart), run_time=1)

        with self.voiceover(text="我有一个好妈妈,我是妈妈的好宝宝，妈妈是我的好妈妈,我爱我的妈妈,妈妈爱我") as tracker:
             for _ in range(30):  # Loop for 3 beats
               self.play(heart.animate.scale(1.2), run_time=0.3)  # Expand
               self.play(heart.animate.scale(1/1.2), run_time=0.3)  # Contract



        with self.voiceover(text="妈妈") as tracker:
            self.play(FadeOut(heart), run_time=tracker.duration)
        
        self.wait(1)

        with self.voiceover(text="妈妈") as tracker:
            self.play(FadeOut(babyPronunciation), run_time=tracker.duration)
        
        self.wait(2)


        with self.voiceover(text="妈妈") as tracker:
            self.play(FadeOut(baby), run_time=tracker.duration)

        self.wait(3)

        with self.voiceover(text="妈妈") as tracker:
            self.play(FadeOut(momPronunciation), run_time=tracker.duration)

        self.wait(4)

        with self.voiceover(text="妈妈") as tracker:
            self.play(FadeOut(mom), run_time=tracker.duration)
            


    def heart_beat(self, heart):
         for _ in range(30):  # Loop for 3 beats
            self.play(heart.animate.scale(1.2), run_time=0.3)  # Expand
            self.play(heart.animate.scale(1/1.2), run_time=0.3)  # Contract

