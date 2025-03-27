import streamlit as st
import random
from datetime import datetime

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
    def __init__(self, niche, product_name, description=None):
        self.niche = niche.lower()
        self.product_name = product_name.lower()
        self.description = description.lower() if description else None
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        self.trends = self.fetch_simulated_trends()

    def fetch_simulated_trends(self):
        return trend_database.get(self.niche, default_trends)

    def generate_caption(self):
        if self.description:
            trend_word = random.choice(self.trends).replace("#", "")
            mood = random.choice(["So cool!", "Loving this!", "Can’t get enough!", "Wow, just wow!"])
            base = f"Hey guys, {self.description} with this {self.product_name}!"
            return f"{base} Totally vibing with {trend_word} feels today. {mood}"
        else:
            trend_word = random.choice(self.trends).replace("#", "")
            mood = random.choice(["Wow!", "Obsessed!", "Must-try!", "Epic!"])
            base = f"Get your {self.product_name} now - perfect for {self.niche} fans!"
            return f"{base} Rocking {trend_word} vibes this {self.current_date}. {mood}"

    def generate_hashtags(self):
        niche_tags = [f"#{self.niche}", f"#{self.niche}Lovers"]
        product_tags = [f"#{self.product_name}", f"#{self.product_name}Addict"]
        if self.description:
            desc_words = self.description.split()
            desc_tags = [f"#{word}" for word in desc_words if len(word) > 3][:2]
            return niche_tags + product_tags + desc_tags + self.trends[:2]
        return niche_tags + product_tags + self.trends[:3]

    def generate_seo_keywords(self):
        base_keywords = [self.product_name, self.niche]
        trend_keywords = [word.replace("#", "").lower() for word in self.trends[:2]]
        if self.description:
            desc_keywords = [word for word in self.description.split() if len(word) > 3][:2]
            return base_keywords + desc_keywords + trend_keywords + ["2025", "best"]
        return base_keywords + trend_keywords + ["2025", "best"]

    def simulate_algorithm_insight(self):
        engagement_score = random.randint(40, 90)
        reach_potential = engagement_score * (len(self.trends) + (2 if self.description else 1))
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

# Custom CSS for attractive UI
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .stTextInput>label, .stSelectbox>label, .stTextArea>label {
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
    }
    .stTextInput>div>input, .stTextArea>div>textarea {
        background-color: #ffffff;
        color: #333333;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff6666;
    }
    .stSuccess {
        background-color: #28a745;
        border-radius: 8px;
        padding: 10px;
    }
    .stSubheader {
        color: #ffd700;
        font-size: 20px;
        font-weight: bold;
    }
    .output-box {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 15px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("✨ Instagram Post Optimizer ✨")
st.write("Elevate your Instagram game with optimized, high-reach posts!")

# Form with premium styling
with st.form(key="optimizer_form"):
    st.markdown("### Fill Your Details")
    username = st.text_input("Your Username", placeholder="e.g., cooluser123")
    id_type = st.selectbox("ID Type", ["Personal", "Business", "Creator"])
    niche = st.text_input("Your Niche", placeholder="e.g., fashion, tech, food")
    product_name = st.text_input("Product Name", placeholder="e.g., sneakers, smartphone")
    description = st.text_area("Optional: Describe Your Post/Reel", 
                              placeholder="e.g., showing off my new look with friends", height=100)
    submit_button = st.form_submit_button(label="Generate Now")

# Output section
if submit_button:
    if niche and product_name:
        optimizer = InstaTrendOptimizer(niche, product_name, description if description else None)
        result = optimizer.optimize()
        st.success("🎉 Your Optimized Instagram Post is Ready!")
        
        st.subheader("Caption")
        st.markdown(f"<div class='output-box'>{result['caption']}</div>", unsafe_allow_html=True)
        
        st.subheader("Hashtags")
        st.markdown(f"<div class='output-box'>{' '.join(result['hashtags'])}</div>", unsafe_allow_html=True)
        
        st.subheader("SEO Keywords")
        st.markdown(f"<div class='output-box'>{' '.join(result['seo_keywords'])}</div>", unsafe_allow_html=True)
        
        st.subheader("Algorithm Insight")
        st.markdown(f"<div class='output-box'>"
                    f"Engagement Score: {result['algorithm_insight']['engagement_score']}<br>"
                    f"Reach Potential: {result['algorithm_insight']['reach_potential']}<br>"
                    f"Recommendation: {result['algorithm_insight']['recommendation']}"
                    f"</div>", unsafe_allow_html=True)
        
        st.write(f"Generated for {id_type} account: @{username}", unsafe_allow_html=True)
    else:
        st.error("Please fill in both Niche and Product Name!")

# Footer
st.markdown("<hr><p style='text-align: center; color: #ffd700;'>Made with ❤️ for Instagram Creators</p>", unsafe_allow_html=True)
