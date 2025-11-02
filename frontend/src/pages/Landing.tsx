import { Link } from 'react-router-dom';
import { Shield, FileText, TrendingUp, ArrowRight, Brain } from 'lucide-react'; // Added Brain icon for consistency
import Header from '../components/layout/Header';

export default function Landing() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-slate-950 text-gray-100 font-sans antialiased">
      <Header />

      {/* Hero Section */}
      <div className="relative overflow-hidden py-24 px-4 sm:px-6 lg:px-8 text-center bg-gray-900/70">
        <div className="relative max-w-4xl mx-auto z-10">
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white mb-6 leading-tight drop-shadow-2xl">
            AI-Powered Global
            <span className="text-blue-400"> FinTech Compliance</span>
          </h1>
          <p className="text-lg md:text-xl text-gray-300 max-w-2xl mx-auto opacity-90 font-medium leading-relaxed">
            Comprehensive regulatory intelligence for financial services. Navigate PSD2, AML/KYC, MiFID II, 
            PCI-DSS, and global fintech regulations with AI-powered compliance monitoring and risk assessment.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center mt-8">
            <Link to="/signup" className="bg-blue-600 text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-blue-700 transition-colors flex items-center justify-center shadow-lg transform hover:-translate-y-1">
              Start Free Trial
              <ArrowRight className="ml-2 w-5 h-5" />
            </Link>
            <Link to="/compliance" className="border-2 border-blue-600 text-blue-300 px-8 py-4 rounded-lg text-lg font-semibold hover:bg-slate-800 transition-colors shadow-lg transform hover:-translate-y-1">
              Learn More
            </Link>
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div className="py-24 px-4 sm:px-6 lg:px-8 bg-gradient-to-br from-gray-900/80 to-slate-950/80">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">
              Why Choose RegScope?
            </h2>
            <p className="text-lg text-gray-300 max-w-2xl mx-auto">
              Enterprise-grade compliance intelligence designed specifically for fintech and financial services.
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center p-6 bg-slate-800 rounded-lg border border-slate-700 shadow-2xl transform hover:-translate-y-2 hover:scale-105 transition-all duration-300 ease-in-out">
              <div className="bg-blue-900/60 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 border border-blue-700/30 shadow-inner">
                <FileText className="text-blue-300 w-8 h-8" />
              </div>
              <h3 className="text-xl font-semibold text-white mb-2">
                FinTech Compliance Analysis
              </h3>
              <p className="text-gray-300">
                AI-powered analysis of policies, agreements, and documentation against PSD2, MiFID II, AML/KYC, and global fintech regulations.
              </p>
            </div>

            <div className="text-center p-6 bg-slate-800 rounded-lg border border-slate-700 shadow-2xl transform hover:-translate-y-2 hover:scale-105 transition-all duration-300 ease-in-out">
              <div className="bg-green-900/60 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 border border-green-700/30 shadow-inner">
                <Shield className="text-green-300 w-8 h-8" />
              </div>
              <h3 className="text-xl font-semibold text-white mb-2">
                Multi-Jurisdiction Monitoring
              </h3>
              <p className="text-gray-300">
                Real-time monitoring across EU, US, UK, Singapore, and global financial regulations with automated compliance reporting.
              </p>
            </div>

            <div className="text-center p-6 bg-slate-800 rounded-lg border border-slate-700 shadow-2xl transform hover:-translate-y-2 hover:scale-105 transition-all duration-300 ease-in-out">
              <div className="bg-purple-900/60 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 border border-purple-700/30 shadow-inner">
                <Brain className="text-purple-300 w-8 h-8" />
              </div>
              <h3 className="text-xl font-semibold text-white mb-2">
                Regulatory Risk Intelligence
              </h3>
              <p className="text-gray-300">
                Advanced AML/KYC screening, transaction monitoring, and proactive risk identification with actionable compliance insights.
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div className="py-24 bg-gradient-to-r from-blue-900 to-blue-950">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">
            Ready to Transform Your FinTech Compliance?
          </h2>
          <p className="text-lg text-blue-100 mb-8 max-w-2xl mx-auto">
            Join leading financial institutions and fintech companies using RegScope for global regulatory compliance.
          </p>
          <Link to="/signup" className="bg-blue-300 text-slate-900 px-8 py-4 rounded-lg text-lg font-semibold hover:bg-blue-200 transition-colors inline-flex items-center shadow-lg transform hover:-translate-y-1">
            Get Started Today
            <ArrowRight className="ml-2 w-5 h-5" />
          </Link>
        </div>
      </div>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12 border-t border-slate-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center mb-4">
                <div className="bg-blue-600 w-8 h-8 flex items-center justify-center rounded-lg shadow-md">
                  <FileText className="text-white w-5 h-5" />
                </div>
                <span className="ml-2 text-xl font-bold">LegalGuard</span>
              </div>
              <p className="text-gray-400">
                AI-powered legal compliance platform for modern businesses.
              </p>
            </div>
            <div>
              <h3 className="text-lg font-semibold mb-4 text-blue-300">Product</h3>
              <ul className="space-y-2 text-gray-400">
                <li><Link to="/compliance" className="hover:text-blue-200 transition-colors">Compliance</Link></li>
                <li><Link to="/regulations" className="hover:text-blue-200 transition-colors">Regulations</Link></li>
                <li><Link to="/signup" className="hover:text-blue-200 transition-colors">Pricing</Link></li>
              </ul>
            </div>
            <div>
              <h3 className="text-lg font-semibold mb-4 text-blue-300">Company</h3>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-blue-200 transition-colors">About</a></li>
                <li><a href="#" className="hover:text-blue-200 transition-colors">Contact</a></li>
                <li><a href="#" className="hover:text-blue-200 transition-colors">Support</a></li>
              </ul>
            </div>
            <div>
              <h3 className="text-lg font-semibold mb-4 text-blue-300">Legal</h3>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-blue-200 transition-colors">Privacy Policy</a></li>
                <li><a href="#" className="hover:text-blue-200 transition-colors">Terms of Service</a></li>
                <li><a href="#" className="hover:text-blue-200 transition-colors">Cookie Policy</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-slate-800 mt-8 pt-8 text-center text-gray-400">
            <p>&copy; 2024 LegalGuard. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}