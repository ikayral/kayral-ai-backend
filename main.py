<div id="kayral-ai-container" style="max-width: 700px; margin: 0 auto;">
  <h2>Kayral AI – Sağlık Yönetimi Asistanı (Beta)</h2>
  <p>
    Aşağıya sağlık yönetimi, hasta güvenliği, kalite ve liderlik ile ilgili sorunuzu yazın.
    Klinik tanı/tedavi sorularına cevap verilmez.
  </p>

  <textarea id="kayral-question" rows="5" style="width: 100%; padding: 10px;"
    placeholder="Örneğin: Yoğun bakımda hasta güvenliğini artırmak için 5 somut adım önerir misin?"></textarea>

  <button id="kayral-send" style="margin-top: 10px; padding: 8px 16px;">
    Soruyu Gönder
  </button>

  <div id="kayral-loading" style="margin-top: 10px; display: none;">
    Yanıt hazırlanıyor, lütfen bekleyin...
  </div>

  <div id="kayral-answer" style="margin-top: 20px; white-space: pre-wrap;"></div>
</div>

<script>
  const BACKEND_URL = "https://kayral-ai-backend-1.onrender.com/ask";

  document.getElementById("kayral-send").addEventListener("click", async () => {
    const questionEl = document.getElementById("kayral-question");
    const answerEl = document.getElementById("kayral-answer");
    const loadingEl = document.getElementById("kayral-loading");

    const question = questionEl.value.trim();
    if (!question) {
      alert("Lütfen önce bir soru yazın.");
      return;
    }

    answerEl.textContent = "";
    loadingEl.style.display = "block";

    try {
      const response = await fetch(BACKEND_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: question }),
      });

      if (!response.ok) {
        throw new Error("Sunucudan geçerli bir yanıt alınamadı.");
      }

      const data = await response.json();
      answerEl.textContent = data.answer || "Yanıt alınamadı.";
    } catch (err) {
      console.error(err);
      answerEl.textContent = "Bir hata oluştu. Lütfen daha sonra tekrar deneyin.";
    } finally {
      loadingEl.style.display = "none";
    }
  });
</script>
