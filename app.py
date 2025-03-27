import streamlit as st
import random
from datetime import datetime
from pyngrok import ngrok

# Simulated trend database
trend_database = {
    "fashion": ["#FashionVibes", "#StyleGoals", "#TrendyLook", "chic", "glam"],
    "tech": ["#TechLife", "#GadgetTrend", "#InnovateNow", "smart", "future"],
    "food": ["#FoodLovers", "#TastyBites", "#YummyTrend", "delicious", "flavor"],
    "fitness": ["#FitLife", "#WorkoutVibes", "#HealthTrend", "strong", "active"],
    "travel": ["#TravelGoals", "#Wanderlust", "#ExploreNow", "adventure", "journey"]
}
default_trends = ["#Trending", "#ViralNow", "#ExploreMore", "new", "hot"]

class InstaTrendOptimizer:
    def __init__(self, niche, product_name):
        self.niche = niche.lower()
        self.product_name = product_name.lower()
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        self.trends = self.fetch_simulated_trends()

    def fetch_simulated_trends(self):
        return trend_database.get(self.niche, default_trends)

    def generate_caption(self):
        trend_word = random.choice(self.trends).replace("#", "")
        mood = random.choice(["Wow!", "Obsessed!", "Must-try!", "Epic!"])
        base = f"Get your {self.product_name} now - perfect for {self.niche} fans! "
        return f"{base}Rocking {trend_word} vibes this {self.current_date}. {mood}"

    def generate_hashtags(self):
        niche_tags = [f"#{self.niche}", f"#{self.niche}Lovers"]
        product_tags = [f"#{self.product_name}", f"#{self.product_name}Addict"]
        return niche_tags + product_tags + self.trends[:3]

    def generate_seo_keywords(self):
        base_keywords = [self.product_name, self.niche]
        trend_keywords = [word.replace("#", "").lower() for word in self.trends[:2]]
        return base_keywords + trend_keywords + ["2025", "best"]

    def simulate_algorithm_insight(self):
        engagement_score = random.randint(40, 90)
        reach_potential = engagement_score * (len(self.trends) + 2)
        recommendation = "Post now for high reach!" if reach_potential > 150 else "Add a call-to-action for better results."
        return {
            "engagement_score": engagement_score,
            "reach_potential": reach_potential,
            "recommendation": recommendation
        }

    def optimize(self):
        return {
            "caption": self.generate_caption(),
            "hashtags": self.generate_hashtags(),
            "seo_keywords": self.generate_seo_keywords(),
            "algorithm_insight": self.simulate_algorithm_insight()
        }

# Streamlit Web App
st.title("Instagram Post Optimizer")
st.write("Enter your details below to get an optimized Instagram post!")

with st.form(key="optimizer_form"):
    username = st.text_input("Your Username", placeholder="e.g., cooluser123")
    id_type = st.selectbox("ID Type", ["Personal", "Business", "Creator"])
    niche = st.text_input("Your Niche (e.g., fashion, tech, food)", placeholder="e.g., fashion")
    product_name = st.text_input("Product Name (e.g., sneakers, smartphone)", placeholder="e.g., sneakers")
    submit_button = st.form_submit_button(label="Generate Optimized Post")

if submit_button:
    if niche and product_name:
        optimizer = InstaTrendOptimizer(niche, product_name)
        result = optimizer.optimize()

        st.success("Here’s your optimized Instagram post!")
        st.subheader("Caption")
        st.write(result["caption"])
        st.subheader("Hashtags")
        st.write(" ".join(result["hashtags"]))
        st.subheader("SEO Keywords")
        st.write(" ".join(result["seo_keywords"]))
        st.subheader("Algorithm Insight")
        st.write(f"Engagement Score: {result['algorithm_insight']['engagement_score']}")
        st.write(f"Reach Potential: {result['algorithm_insight']['reach_potential']}")
        st.write(f"Recommendation: {result['algorithm_insight']['recommendation']}")
        st.write(f"Generated for {id_type} account: @{username}")
    else:
        st.error("Please fill in both Niche and Product Name!")

# Ngrok ke saath public URL
public_url = ngrok.connect(8501)
st.write(f"Access your app at: {public_url}")