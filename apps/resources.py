import streamlit as st

def resources_page():
    # st.subheader("📚 Resources & Documentation", divider='green')
    
    # Project Information
    st.markdown("### 🎓 Project Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Project Title:** Cloud-Native Credit Card Fraud Detection
        
        **Team:** Group 4
        - Cecil Oiku
        - Katelyn Siu  
        - Israel Maikyau
        - Meet Patel
        
        **Institution:** University of Calgary
        
        **Course:** DATA 695
        """)
    
    with col2:
        st.markdown("""
        **Technologies Used:**
        - Python & TensorFlow/Keras
        - Microsoft Azure ML Studio
        - Streamlit Web Framework
        - Scikit-learn & Pandas
        - Power BI Visualizations
        
        **Datasets:**
        - European Credit Card Dataset (Real)
        - Financial Transactions Dataset (Synthetic)
        """)
    
    st.markdown("---")
    
    # Research Papers & References
    st.markdown("### 📖 Research Papers & References")
    
    papers_data = [
        {
            "title": "Enhanced credit card fraud detection model using machine learning",
            "authors": "Al-Hashemi, R. R., & Al-Mosawi, A. I.",
            "journal": "Electronics, 11(4), 662",
            "year": "2022",
            "link": "https://doi.org/10.3390/electronics11040662"
        },
        {
            "title": "Enhanced credit card fraud detection based on attention mechanism and LSTM deep model", 
            "authors": "Benchaji, I., Douzi, S., & El Ouahidi, B.",
            "journal": "Journal of Big Data, 8(1), 151",
            "year": "2021",
            "link": "https://doi.org/10.1186/s40537-021-00541-8"
        },
        {
            "title": "A supervised machine learning algorithm for detecting and predicting fraud in credit card transactions",
            "authors": "Awoyemi, J. O., Adetunmbi, A. O., & Oluwadare, S. A.",
            "journal": "Machine Learning with Applications, 9, 100359",
            "year": "2023", 
            "link": "https://doi.org/10.1016/j.mlwa.2022.100359"
        },
        {
            "title": "Credit card fraud detection: A deep learning approach",
            "authors": "Sharma, A., & Kumar, S.",
            "journal": "arXiv preprint arXiv:2409.13406v1",
            "year": "2024",
            "link": "https://arxiv.org/abs/2409.13406v1"
        }
    ]
    
    for paper in papers_data:
        with st.expander(f"📄 {paper['title']} ({paper['year']})"):
            st.markdown(f"**Authors:** {paper['authors']}")
            st.markdown(f"**Published in:** {paper['journal']}")
            st.markdown(f"**Year:** {paper['year']}")
            st.markdown(f"**Link:** [{paper['link']}]({paper['link']})")
    
    st.markdown("---")
    
    # Technical Documentation
    st.markdown("### 🔧 Technical Documentation")
    
    tab1, tab2, tab3 = st.tabs(["Model Architecture", "Dataset Information", "Performance Metrics"])
    
    with tab1:
        st.markdown("""
        #### Neural Network Architecture
        
        **European Dataset Model:**
        - Input Layer: 29 features (V1-V28 + Amount)
        - Hidden Layers: 256 → 128 → 64 → 32 → 16 → 8 neurons
        - Activation: ReLU (hidden), Sigmoid (output)
        - Regularization: BatchNormalization + Dropout
        - Optimizer: Adam (lr=0.001)
        
        **Synthetic Dataset Model:**
        - Input Layer: 12 features (transaction details + engineered features)
        - Hidden Layers: 256 → 128 → 64 → 32 → 16 → 8 neurons
        - Same architecture as European model
        - Additional preprocessing: SMOTE balancing
        """)
    
    with tab2:
        st.markdown("""
        #### Dataset Characteristics
        
        **European Credit Card Dataset:**
        - Source: Real European cardholder transactions (2023)
        - Size: 568,630 transactions
        - Features: 29 (V1-V28 PCA features + Amount)
        - Class Distribution: 50-50 balanced (artificially)
        - Quality: High-quality, preprocessed data
        
        **Synthetic Financial Dataset:**
        - Source: Generated financial transaction data
        - Size: 538,659 transactions (after cleaning)
        - Features: 12 (transaction details + risk scores)
        - Class Distribution: 1:2 fraud to legitimate ratio
        - Challenges: Limited predictive signals
        """)
    
    with tab3:
        st.markdown("""
        #### Model Performance Comparison
        
        | Metric | European Model | Synthetic Model |
        |--------|----------------|-----------------|
        | Accuracy | 95.68% | 53.00% |
        | Precision | 97.56% | 33.37% |
        | Recall | 93.71% | 41.11% |
        | F1-Score | 95.59% | 36.83% |
        | AUC-ROC | 99.08% | 49.93% |
        | Avg Precision | 99.22% | 33.22% |
        """)

        st.markdown("")
                                    
        st.markdown("""
                **Key Insights:**
                - European model shows excellent performance across all metrics
                - Synthetic model performs at random chance level
                - Real-world PCA features significantly outperform synthetic features
                """)
    
    st.markdown("---")
    
    # GitHub Repository
    st.markdown("### 💻 Code Repository")
    
    st.info("""
    **GitHub Repository: https://github.com/thebugged/credit-card-fraud**
    
    The complete source code, datasets, trained models, and documentation are available in our GitHub repository.
    This includes:
    - Data preprocessing scripts
    - Model training notebooks  
    - Evaluation metrics and visualizations
    - Streamlit application code
    - Technical report and presentation
    """)
    
    # st.markdown("---")
    
    # # Contact Information
    # st.markdown("### 📧 Contact Information")
    
    # st.markdown("""
    # For questions about this project or collaboration opportunities:
    
    # **Team Members:**
    # - **Cecil Oiku:** [email]
    # - **Katelyn Siu:** [email]  
    # - **Israel Maikyau:** [email]
    # - **Meet Patel:** [email]
    
    # **Project Supervisor:** [Supervisor Name & Email]
    # """)

if __name__ == "__main__":
    resources_page()